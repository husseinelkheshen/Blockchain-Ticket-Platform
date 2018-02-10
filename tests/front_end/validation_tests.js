// Testing suite design for use by Jasmine framework

describe("Test for validation of names", function() {

    // Valid Name input requriements
    /*  1. Names cannot be empty
        2. Names must be between 1 and 128 characters (under 129 characters)
        3. Names should contain alpha characters
        4. Names may be capitalized in any manner
        5. Names can contain hyphens '-' and spaces ' '
        6. Names cannot start or end with a space
        7. Names may contain special alpha characters only (ie á, î, ü,
            etc, but not non alpha special characters like ©,^,ƒ,√, etc.)
    */

    /* Postitive Validation Tests*/
    it("tests positive validation of lowercase alpha character name inputs", function() {
        var a = validName("samantha");
        expect(a).toBe(true);
    });
    it("tests positive validation of all lowercase alpha characters", function() {
        var a = validName("abcdefghijklmnopqrstuvwxyz");
        expect(a).toBe(true);
    });
    it("tests for positive validation of uppercase alpha character name inputs", function() {
        var a = validName("REY");
        expect(a).toBe(true);
    });
    it("tests positive validation of all uppercase alpha characters", function() {
        var a = validName("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
        expect(a).toBe(true);
    });
    it("tests for positive validation of upper/lowercase alpha character name inputs", function() {
        var a = validName("SamanthaTSRey");
        expect(a).toBe(true);
    });
    it("tests for positive validation of alpha character inputs with hypen '-' character ", function() {
        var a = validName("Tai-yang");
        expect(a).toBe(true);
    });
    it("tests for positive validation of alpha character inputs with space ' ' character ", function() {
        var a = validName("Shih Rey");
        expect(a).toBe(true);
    });
    it("tests for positive validation of alpha character inputs with space ' 'and hyphen '-' characters", function() {
        var a = validName("Samantha Tai-yang Shih Rey");
        expect(a).toBe(true);
    });
    it("tests for positive validation of alpha characters with special alpha characters", function() {
        var a = validName("Màrcio Fortunella");
        expect(a).toBe(true);
    });
    it("tests for positive validation of alpha characters with special alpha characters and spaces and hypens", function() {
        var a = validName("ÁBCDE--efg   HÏJK");
        expect(a).toBe(true);
    });
    it("tests for positive validation of 1 character name", function() {
        var a = validName("a");
        expect(a).toBe(true);
    });
    it("tests for positive validation of 128 character name", function() {
        var a = validName("Esteban Julio Ricardo Montoya De-la-Rosa Ramiréz the XXXVth abcdefghigjklmnopqrstuvwxyzabcdefghigjklmnopqrstuvwxyzabcdefghigjklm");
        expect(a).toBe(true);
    });
    

    /* Negative Validation Tests */
    //Fails condition 1
    it("tests for negative validation of empty name", function() {
        var a = validName(null);
        expect(a).toBe(false);
    });
    //Fails condition 1 and 2
    it("tests for negative validation of 0 character name", function() {
        var a = validName("");
        expect(a).toBe(false);
    });
    //Fails condition 2
    it("tests for negative validation of 128 character name", function() {
        var a = validName("Esteban Julio Ricardo Montoya De-la-Rosa Ramiréz the XXXVth abcdefghigjklmnopqrstuvwxyzabcdefghigjklmnopqrstuvwxyzabcdefghigjklmn");
        expect(a).toBe(false);
    });
    //Fails condtion 3
    it("tests for negative validation of name with numeric characters", function() {
        var a = validName("6");
        expect(a).toBe(false);
    });
    // Fails condition 3
    it("tests for negative validation of name with alphanumeric characters", function() {
        var a = validName("S4M");
        expect(a).toBe(false);
    });
    // Fails condtions 3 and 7
    it("tests for negative validation of name with special non-alpha characters, test 1", function() {
        var a = validName(".");
        expect(a).toBe(false);
    });
    // Failis conditions 3 and 7, this is partially redundant, but there are two classes of special characters
    // So I thought it would be somewhat worthwile to check, sonsidering special alpha characters fall in the
    // a different class of special characters than the special characters on visible keys
    it("tests for negative validation of name with special non-alpha characters, test 2", function() {
        var a = validName("©");
        expect(a).toBe(false);
    });
    // Fails condiitons 3 and 7
    it("tests for negative validation of name with alpha and non-alpha special characters, test 1", function() {
        var a = validName("S@M");
        expect(a).toBe(false);
    });
    // Fails conditions 3 and 7
    it("tests for negative validation of name with non-alpha special characters, test 2", function() {
        var a = validName("Samantha ®ey");
        expect(a).toBe(false);
    });
    // Fails Condition 6
    it("tests for negative validation of name starting with spaces", function() {
        var a = validName(" Sam");
        expect(a).toBe(false);
    });
    // Fails Condition 6
    it("tests for negative validation of name ending with spaces", function() {
        var a = validName("Sam ");
        expect(a).toBe(false);
    });
    // Fails Condition 6
    it("tests for negative validation of name starting and ending with spaces", function() {
        var a = validName(" ");
        expect(a).toBe(false);
    });

});









describe("Test for validation of local address in email", function() {

    // Valid local email address (the part of the email up to the '@')
    /* 1. Cannot be empty
       2. Must be between 1 and 64 characters
       3. Can contain Uppercase and lowercase English letters (a-z, A-Z)
       4. Can contain Digits 0 to 9
       5. Can contain Characters ! # $ % & ' * + - / = ? ^ _ ` { | } ~
       6. Can contain period '.' provided that it is not the first or last character,
            and provided also that it does not appear two or more times consecutively.

    /* Postitive Validation Tests*/
    it("tests positive validation of lowercase alpha character inputs", function() {
        var a = validLocal("samantha");
        expect(a).toBe(true);
    });
    it("tests for positive validation of all allowed uppercase alpha characters in input", function() {
        var a = validLocal("abcdefghijklmnopqrstuvwxyz");
        expect(a).toBe(true);
    });
    it("tests for positive validation of uppercase alpha character inputs", function() {
        var a = validLocal("REY");
        expect(a).toBe(true);
    });
    it("tests for positive validation of all allowed uppercase alpha characters in input", function() {
        var a = validLocal("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
        expect(a).toBe(true);
    });
    it("tests for positive validation of upper/lowercase alpha character inputs", function() {
        var a = validLocal("SamanthaTSRey");
        expect(a).toBe(true);
    });
    it("tests for positive validation of alphanumeric character inputs", function() {
        var a = validLocal("s4m");
        expect(a).toBe(true);
    });
    it("tests for positive validation of all allowed numeric characters in input", function() {
        var a = validLocal("0123456789");
        expect(a).toBe(true);
    });
    it("tests for positive validation of alphanumeric and special character inputs", function() {
        var a = validLocal("s4m!");
        expect(a).toBe(true);
    });
    it("tests for positive validation of all valid special chracters", function() {
        var a = validLocal("!#$%&'*+-/=?^_`{|}~");
        expect(a).toBe(true);
    });
    it("tests for positive validation for valid '.' placement in input", function() {
        var a = validLocal("samantha.rey");
        expect(a).toBe(true);
    });
    it("tests for positive validation of 1 character input", function() {
        var a = validLocal("a");
        expect(a).toBe(true);
    });
    it("tests for positive validation of 64 character input", function() {
        var a = validLocal("samantha.tai-yang.shih.rey.abcdefghijklmnopqrstuvwxyz0123456789*");
        expect(a).toBe(true);
    });


    /* Negative Validation Tests */
    // Fails condition 1
    it("tests for negative validation of empty input", function() {
        var a = validLocal(null);
        expect(a).toBe(false);
    });
    // Fails conditions 1 and 2
    it("tests for negative validation of 0 character input", function() {
        var a = validLocal("");
        expect(a).toBe(false);
    });
    // Fails condition 2
    it("tests for negative validation of 65 character input", function() {
        var a = validLocal("samantha.tai-yang.shih.rey.abcdefghijklmnopqrstuvwxyz0123456789**");
        expect(a).toBe(false);
    });
    // Fails condition 5
    it("tests for negative validation of other special characters", function() {
        var a = validLocal("abcdefg@abcdefg");
        expect(a).toBe(false);
    });
    // Fails condition 6
    it("tests for negative validation of '.' at beginning", function() {
        var a = validLocal(".samantha_rey");
        expect(a).toBe(false);
    });
    // Fails condition 6
    it("tests for negative validation of '.' at end", function() {
        var a = validLocal("samantha_rey.");
        expect(a).toBe(false);
    });
    // Fails condition 6
    it("tests for negative validation of two '.' characters in a row", function() {
        var a = validLocal("abcdefg..abcdefg");
        expect(a).toBe(false);
    });

});


describe("Test for validation of host address in email", function() {

    // Valid host portion of email address (the part of the email after the '@')
    /* 1. Must not be empty
       2. Must be between 1 and 253 characters
       3. May contain Uppercase and Lowercase Latin letters A to Z and a to z
       4. May contain Digits 0 to 9
       5. May contain hyphens '-', provided that it is not the first or last character
       6. Must contain 1 or more periods '.'. It must not be the first or last character
            and two or more do not appear consecutively.
    */

    /* Postitive Validation Tests*/
    it("tests positive validation of lowercase alpha character inputs", function() {
        var a = validHost("samantha.rey");
        expect(a).toBe(true);
    });
    it("tests for positive validation of all allowed uppercase alpha characters in input", function() {
        var a = validHost("abcdefg.hijklmnopqrstuvwxyz");
        expect(a).toBe(true);
    });
    it("tests for positive validation of uppercase alpha character inputs", function() {
        var a = validHost("SAM.REY");
        expect(a).toBe(true);
    });
    it("tests for positive validation of all allowed uppercase alpha characters in input", function() {
        var a = validHost("ABCDEFG.HIJKLMNOPQRSTUVWXYZ");
        expect(a).toBe(true);
    });
    it("tests for positive validation of upper/lowercase alpha character inputs", function() {
        var a = validHost("Samantha.TSRey");
        expect(a).toBe(true);
    });
    it("tests for positive validation of alphanumeric character inputs", function() {
        var a = validHost("s4m.8ey");
        expect(a).toBe(true);
    });
    it("tests for positive validation of all allowed numeric characters in input", function() {
        var a = validHost("01234.56789");
        expect(a).toBe(true);
    });
    it("tests for positive validation for valid '.' placement in input", function() {
        var a = validHost("samantha.rey");
        expect(a).toBe(true);
    });
    it("tests for positive validation for multiple valid '.' placements in input", function() {
        var a = validHost("samantha.taiyang.rey");
        expect(a).toBe(true);
    });
    it("tests for positive validation for valid '-' placement in input", function() {
        var a = validHost("samanthatai-yang.rey");
        expect(a).toBe(true);
    });
    it("tests for positive validation for multiple valid '-' and '.' placements in input", function() {
        var a = validHost("samantha.tai-yang.shih-rey");
        expect(a).toBe(true);
    });
    it("tests for positive validation for 3 character input", function() {
        var a = validHost("s.r");
        expect(a).toBe(true);
    });
    it("tests for positive validation for 253 character input", function() {
        var a = validHost("samantha.tai-yang.shih.rey.abcdefghijklmnopqrstuvwxyz0123456789.samantha.tai-yang.shih.rey.abcdefghijklmnopqrstuvwxyz0123456789.samantha.tai-yang.shih.rey.abcdefghijklmnopqrstuvwxyz0123456789.samantha.tai-yang.shih.rey.abcdefghijklmnopqrstuvwxyz01234567");
        expect(a).toBe(true);
    });

    /* Negative Validation Tests */
    // Fails condition 1
    it("tests for negative validation of empty input", function() {
        var a = validHost(null);
        expect(a).toBe(false);
    });
    // Fails conditions 1 and 2
    it("tests for negative validation of 0 character input", function() {
        var a = validHost("");
        expect(a).toBe(false);
    });
    // Fails condition 2
    it("tests for negative validation of 254 character input", function() {
        var a = validHost("samantha.tai-yang.shih.rey.abcdefghijklmnopqrstuvwxyz0123456789.samantha.tai-yang.shih.rey.abcdefghijklmnopqrstuvwxyz0123456789.samantha.tai-yang.shih.rey.abcdefghijklmnopqrstuvwxyz0123456789.samantha.tai-yang.shih.rey.abcdefghijklmnopqrstuvwxyz012345678");
        expect(a).toBe(false);
    });
    // Fails condition 3 and 4
    it("tests for negative validation of for special characters in input", function() {
        var a = validHost("abcdefg,abcdefg");
        expect(a).toBe(false);
    });
    // Fails conditions 5
    it("tests for negative validation of '-' character at start", function() {
        var a = validHost("-sam.rey");
        expect(a).toBe(false);
    });
    // Fails conditions 6
    it("tests for negative validation of '-' character at end", function() {
        var a = validHost("sam.rey-");
        expect(a).toBe(false);
    });
    // Fails condition 5
    it("tests for negative validation of two '-' characters in a row", function() {
        var a = validHost("abcdefg.--.abcdefg");
        expect(a).toBe(false);
    });
    // Fails conditions 6
    it("tests for negative validation of no '.'' character", function() {
        var a = validHost("samrey");
        expect(a).toBe(false);
    });
    // Fails conditions 6
    it("tests for negative validation of '.' character at start", function() {
        var a = validHost(".samrey");
        expect(a).toBe(false);
    });
    // Fails conditions 6
    it("tests for negative validation of '.' character at end", function() {
        var a = validHost("samrey.");
        expect(a).toBe(false);
    });
    // Fails conditions 6
    it("tests for negative validation of '.' multiple times in a row", function() {
        var a = validHost("sam..rey");
        expect(a).toBe(false);
    });
    // Fails condition 6
    it("tests for negative validation of '.' at beginning", function() {
        var a = validHost(".samantha-rey");
        expect(a).toBe(false);
    });
    // Fails condition 6
    it("tests for negative validation of '.' at end", function() {
        var a = validHost("samantha-rey.");
        expect(a).toBe(false);
    });
    // Fails condition 6
    it("tests for negative validation of two '.' characters in a row", function() {
        var a = validHost("abcdefg..abcdefg");
        expect(a).toBe(false);
    });

});

describe("Test for validation of email address", function() {

    // Valid email address (the part of the email after the '@')
    /* 1. Must not be empty
       2. Must have between 1 and 255 characters
       3. Must contain exactly one '@' symbol
       4. Must contain a valid local address before the '@'
            and a valid host after the '@'
    */

    /* Postitive Validation Tests*/
    it("tests for positive validation valid email", function() {
        var a = validEmail("samantha.rey@samantha.rey");
        expect(a).toBe(true);
    });
    it("tests for valid short email", function() {
        var a = validEmail("s@s.r");
        expect(a).toBe(true);
    });
    it("tests for valid 255 character email", function() {
        var a = validEmail("sinking!rowboats@ABCDEFG.HIJKLMNOPQRSTUVWXYZ.ABCDEFG.HIJKLMNOPQRSTUVWXYZ.ABCDEFG.HIJKLMNOPQRSTUVWXYZ.ABCDEFG.HIJKLMNOPQRSTUVWXYZ.ABCDEFG.HIJKLMNOPQRSTUVWXYZ.ABCDEFG.HIJKLMNOPQRSTUVWXYZ.ABCDEFG.HIJKLMNOPQRSTUVWXYZ.ABCDEFG.HIJKLMNOPQRSTUVWXYZHIJKLMNOPQRSTUV");
        expect(a).toBe(true);
    });
    it("tests for positive validation of all allowed uppercase alpha characters in input", function() {
        var a = validEmail("ABCDEFG.HIJKLMNOPQRSTUVWXYZ");
        expect(a).toBe(true);
    });


    /* Negative Validation Tests */
    // Fails condition 1
    it("tests for negative validation of empty input", function() {
        var a = validEmail(null);
        expect(a).toBe(false);
    });
    // Fails conditions 1 and 2
    it("tests for negative validation of 0 character input", function() {
        var a = validEmail("");
        expect(a).toBe(false);
    });
    // Fails condition 2
    it("tests for negative validation of 256 character input", function() {
        var a = validEmail("sinking!rowboats@ABCDEFG.HIJKLMNOPQRSTUVWXYZ.ABCDEFG.HIJKLMNOPQRSTUVWXYZ.ABCDEFG.HIJKLMNOPQRSTUVWXYZ.ABCDEFG.HIJKLMNOPQRSTUVWXYZ.ABCDEFG.HIJKLMNOPQRSTUVWXYZ.ABCDEFG.HIJKLMNOPQRSTUVWXYZ.ABCDEFG.HIJKLMNOPQRSTUVWXYZ.ABCDEFG.HIJKLMNOPQRSTUVWXYZHIJKLMNOPQRSTUVW");
        expect(a).toBe(false);
    });
    // Fails condition 3
    it("tests for negative validation of no '@' character", function() {
        var a = validEmail("abcdefg.abcdefg");
        expect(a).toBe(false);
    });
    // Fails conditions 4
    it("tests for negative validation of invalid local address", function() {
        var a = validEmail("s[am]rey@uchicago.edu");
        expect(a).toBe(false);
    });
    /// Fails conditions 4
    it("tests for negative validation of invalid host address", function() {
        var a = validEmail("sam-rey@uchicagoedu");
        expect(a).toBe(false);
    });
    // Fails condition 4
    it("tests for negative validation of invalid local and host addresses ", function() {
        var a = validHost("s[am]rey@uch!cago.edu");
        expect(a).toBe(false);
    });
});


