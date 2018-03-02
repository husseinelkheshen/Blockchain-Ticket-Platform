var data = [{"info": "hi"},  {"info": "yo"}, {"info": "hi"},{"info": "hi"},{"info": "hi"},{"info": "hi"},{"info": "hi"},{"info": "hi"},{"info": "hi"},{"info": "hi"},{"info": "hi"},];

function display_block_info(data) {
	remove_block_info()
	$("#visualization-info-list").append("<li class='col-12 mb-1'><strong>Block ID: </strong> {BLOCK ID}</li>" +
		"<li class='col-12 col-sm-6 mb-1'><strong>Previous Hash: </strong> {PREV HASH}</li>" + 
		"<li class='col-12 col-sm-6 mb-1'><strong>Nonce: </strong> {NONCE}</li>" + 
		"<li class='col-12 col-sm-6 mb-1'><strong>Hash: </strong> {HASH}</li>" + 
		"<li class='col-12 col-sm-6 mb-1'><strong>Time Generated: </strong> {MM/DDYYYY HH24:MM}</li>" + 
		"<li class='col-12 col-sm-6 mb-1'><strong>Value: </strong> ${VALUE}</li>");
}
function display_transaction_info(data) {
	remove_block_info()
	$("#visualization-info-list").append("<li class='col-12 mb-1'><strong>Transaction ID: </strong> {TRANSACTION ID}</li>" +
		"<li class='col-12 col-sm-6 mb-1'><strong>Value: </strong> ${VALUE}</li>");
}
function remove_block_info(){
	$("#visualization-info-list").empty();
}

var block_containers = d3.select(".ticket-visualization")
  .selectAll("div")
  .data(data)
    .enter()
    .append('div')
	.attr('class', 'block-container')
	.attr('id', function(d,i) { return 'block-' + i.toString()});

block_containers.append('div')
	.attr('class', function(d,i) {
 		if(i == 0) {
 			return 'invisible-arrow';
 		}
 		else {
 			return 'end-arrow';
 		}
 	})
 	.attr('id', function(d,i) {
 		if(i > 0) {
 			return 'end-' + (i-1).toString() + '-to-' + i.toString();
 		}
 		else {
 			return '';
 		}
 	})
 	.style('background-image', function(d,i) {
 		if(i == 0) {
 			return '';
 		}
 		else {
 			return "url('images/arrow-end.png')";
 		}
 	})
 	.style('background-repeat', 'no-repeat')
 	.style('background-position', 'center')
 	.style('background-size', 'contain')
 	.on("mouseover", function(d,i) {
 		if(i != 0) {
 			display_transaction_info(d);
 		}
 	})
 	.on("mouseout", function() {
 		remove_block_info();
 	});

block_containers.append('div')
	.attr('class', 'block')
	.text(function(d,i) {
		return i;
	})
	.on("mouseover", function(d) {
		display_block_info(d);

	})
	.on("mouseout",  function() {
		remove_block_info();
	});/*
	.on("mousemove", function(d) {
		var xPos = d3.mouse(this)[0] - 15;
		var yPos = d3.mouse(this)[1] - 55;
		tooltip.attr("transform", "translate(" + xPos + "," + yPos + ")");
		tooltip.select("text").text("Hello World")
	});*/

/*
var tooltip = block_containers.append("div")
				.attr("class", "tooltip");
				//.style("display", "none");
				*/

//tooltip.append("text");
	

block_containers.append('div')
	.attr('class', function(d,i) {
		if(i == data.length -1) {
			return'invisible-arrow';
		}
		else {
			return 'start-arrow';
		}
	})
	.attr('id', function(d,i) {
 		if(i != data.length -1) {
 			return 'start-' + i.toString() + '-to-' + (i+1).toString();
 		}
 		else {
 			return '';
 		}
 	})
 	.style('background-image', function(d,i) {
 		if(i == data.length-1) {
 			return '';
 		}
 		else {
 			return "url('images/arrow-start.png')";
 		}
 	})
 	.style('background-repeat', 'no-repeat')
 	.style('background-position', 'center')
 	.style('background-size', 'contain')
 	.on("mouseover", function(d,i) {
 		if(i != data.length-1) {
 			display_transaction_info(d);
 		}
 	})
 	.on("mouseout", function() {
 		remove_block_info();
 	});



 for(i = 0; i < data.length - 1; i++) {
 	$('#start-' + i.toString() + '-to-' + (i+1).toString()).hover(
		function() {
		    $(this).stop().fadeTo(200, 1);
		    var id = $(this).attr('id');
		    var endid = '#end' + id.substring(5, id.length);
		    $(endid).stop().fadeTo(200,1);


		},
		function() {
		    $(this).stop().fadeTo(200, .5);
		    var id = $(this).attr('id');
		    var endid = '#end' + id.substring(5, id.length);
		    $(endid).stop().fadeTo(200,.5);
		}
	);

	$('#end-' + i.toString() + '-to-' + (i+1).toString()).hover(
		function() {
		    $(this).stop().fadeTo(200, 1);
		    var id = $(this).attr('id');
		    var startid = '#start' + id.substring(3, id.length);
		    $(startid).stop().fadeTo(200,1);

		},
		function() {
		    $(this).stop().fadeTo(200, .5);
		    var id = $(this).attr('id');
		    var startid = '#start' + id.substring(3, id.length);
		    $(startid).stop().fadeTo(200,.5);
		}
	);
 }
/*
d3.selectAll("block-container")
	.data(data)
	.enter()
	.append('div')
	.attr('class', 'block')
	.text(function(d,i) { return i; });
	
d3.selectAll("block-container")
	.data(data)
	.enter()
	.append('div')
	 	.attr('class', function(d,i) {
 			if(i == data.length -1) {
 				return 'invisible';
 			}
 			else {
 				return'start-arrow';
 			}
 		})

*/