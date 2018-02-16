/* validate name inputs */
function validName(name) {
	 // Valid Name input requriements
    /*  1. Names cannot be empty
        2. Names must be between 1 and 128 characters (under 129 characters)
        3. Names may contain alpha characters
        4. Names may be capitalized in any manner
        5. Names can contain hyphens '-' and spaces ' '
        6. Names cannot start or end with a space

        NOTE: Removed requirement 7 from the validation as it poses a 
        security concern for XSS attacks, and picking
        and choosing which special characters
        for names would be allowed wasn't worth the hassle.
        ----7. Names may contain special alpha characters ()
            etc, but not non alpha special characters like ©,^,ƒ,√, etc.)-----
    */

    /* Invalidate names that do not meet condition 1*/
    if(!notEmpty(name)) {
		return false;
	}

	/* Invalidate names that do not meet condition 2 */
	if(name.length < 0 || name.length > 128) {
		return false;
	}

	/* Invalidate names that do not meet conditions 3, 4, 5, and part of 6 */
	if(name.search(/[^a-zA-Z \-]/) >= 0) {
		return false;
	}

	/* Invalidates names that do not meet the remaining part of condition 6,
	 * That a name cannot start and end with a space ' ' */
	if(name.search(/(^ | $)/) >= 0) {
		return false;
	}

	return true;

}

/* validate the local address portion of email addresses */
function validLocal(localaddr) {
	//Requirements
    /* 1. Cannot be empty
       2. Must be between 1 and 64 characters
       3. Can contain Uppercase and lowercase English letters (a-z, A-Z)
       4. Can contain Digits 0 to 9
       5. Can contain Characters ! # $ % & ' * + - / = ? ^ _ ` { | } ~
       6. Can contain period '.' provided that it is not the first or last character,
            and provided also that it does not appear two or more times consecutively.
    */

	/* Invalidate local adresses that do not meet condition 1 */
	if(!notEmpty(localaddr)) {
		return false;
	}


	/* Invalidate names that do not meet condition 2 */
	if (localaddr.length < 1 || localaddr.length > 64) {
		return false;
	}

	/* Invalidates local addresses that do not meet conditions 3, 4, 6, and part of 6 */
	var re = /[^a-zA-Z0-9 !#\$%&'\*\+-/=?\^_`\{\|\}\~\.]/;
	if(localaddr.search(re) >= 0) {
		return false;
	}

	/* Invalidates the second part of condition 6, that strings don't start or end with
	 * a '.'' */
	if(localaddr.search(/(^\.|\.$)/) >= 0) {
		return false;
	}

	/* Invalidates the final part of condition 6, that . does not appear two or more times cosecutively */

	if(localaddr.search(/\.\./) >= 0) {
		return false;
	}

	return true;


}

/* validate the host address portion of email addresses */
function validHost(hostaddr) {
	// Valid host portion of email address (the part of the email after the '@')
    /* 1. Must not be empty
       2. Must be between 1 and 253 characters
       3. May contain Uppercase and Lowercase Latin letters A to Z and a to z
       4. May contain Digits 0 to 9
       5. May contain hyphens '-', provided that it is not the first or last character
       6. Must contain 1 or more periods '.'. It must not be the first or last character
            and two or more do not appear consecutively.
    */


    /* Invalidate host adresses that do not meet condition 1 */
	if(!notEmpty(hostaddr)) {
		return false;
	}

	/* Invalidate host adresses that do not meet condition 2 */
	if(hostaddr.length < 1 || hostaddr.length > 253) {
		return false;
	}

	/* Invalidate host adresses that do not meet conditions 3, 4, part of 5, and part of 6 */
	var re = /[^a-zA-Z0-9-\.]/;
	if(hostaddr.search(re) >= 0) {
		return false;
	}

	/* Invalidate host adresses that do not meet the remainder of condition 5,
	 * that the host address cannot start or end with a '-' */
	if(hostaddr.search(/(^\-|\-$)/) >= 0) {
		return false;
	}

	/* Invalidate host adresses that do not meet the second part of condition 6,
	 * that the host address cannot start or end with a '.' */
	if(hostaddr.search(/(^\.|\.$)/) >= 0) {
		return false;
	}

	/* Invalidate host adresses that do not meet the third part of condition 6,
	 * that the host address must contain a '.'  */
	if(hostaddr.search(/\./) < 0) {
		return false;
	}

	/* Invalidate host adresses that do not meet the remainder of condition 6,
	 * that there must not be more than one '.' in a row */
	if(hostaddr.search(/\.\./) >= 0) {
		return false;
	}

	return true;
}

/* validate email addresses */
function validEmail(email) {
	// Valid email address (the part of the email after the '@')
    /* 1. Must not be empty
       2. Must have between 1 and 255 characters
       3. Must contain exactly one '@' symbol
       4. Must contain a valid local address before the '@'
            and a valid host after the '@'
    */
	
	/* Invalidate email adresses that do not meet condition 1 */
	if(!notEmpty(email)) {
		return false;
	}

	/* Invalidate email adresses that do not meet condition 2 */
	if(email.length < 1 || email.length > 255) {
		return false;
	}

	/* Invalidate email adresses that do not meet condition 3, 
	 * and grab which location the '@' symbol is at if it is in the 
	 * email address */
	var indexAt = email.search(/@/);
	if( indexAt < 0) {
		return false;
	}

	/* slice email address into local and host address portions */
	var localaddr = email.slice(0, indexAt);
	var hostaddr = email.slice(indexAt+1, email.length);


	/* NOTE: while technically there is no case catching  the presence
	 * of more than one @ explicitly, the since localaddr and 
	 * host addr reject inputs with '@' characters, if there is more than 
	 * one '@' character, it will be caught by validLocal and valid Host
	 */

	 /* Invalidate email adresses that do not meet condition 4 */
	if(!(validLocal(localaddr) && validHost(hostaddr))) {
		return false;
	}


	return true; 


}


/* helper function to determine if a string is empty,
 * since it is tested for so many times */
function notEmpty(str) {
	if(str == null || str === "") {
		return false;
	}
	return true;

}