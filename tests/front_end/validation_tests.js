// Testing suite design for use by Jasmine framework

describe("Test for validation of names", function() {

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
        ----7. Names may contain special alpha characters only (ie á, î, ü,
            etc, but not non alpha special characters like ©,^,ƒ,√, etc.)----
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

    /* !!!!!!! Removed tests due to removal of the 7th requirement  !!!!!!!! */
    // it("tests for positive validation of alpha characters with special alpha characters", function() {
    //     var a = validName("Màrcio Fortunella");
    //     expect(a).toBe(true);
    // });
    // it("tests for positive validation of alpha characters with special alpha characters and spaces and hypens", function() {
    //     var a = validName("ÁBCDE--efg   HÏJK");
    //     expect(a).toBe(true);
    // });
    it("tests for positive validation of 1 character name", function() {
        var a = validName("a");
        expect(a).toBe(true);
    });
    it("tests for positive validation of 128 character name", function() {
        var a = validName("Esteban Julio Ricardo Montoya De-la-Rosa Ramirez the XXXVth abcdefghigjklmnopqrstuvwxyzabcdefghigjklmnopqrstuvwxyzabcdefghigjklm");
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
        var a = validName("Esteban Julio Ricardo Montoya De-la-Rosa Ramirez the XXXVth abcdefghigjklmnopqrstuvwxyzabcdefghigjklmnopqrstuvwxyzabcdefghigjklmn");
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
    // Fails condtions 3
    it("tests for negative validation of name with special characters, test 1", function() {
        var a = validName(".");
        expect(a).toBe(false);
    });
    // Fails conditions 3
    it("tests for negative validation of name with special characters, test 2", function() {
        var a = validName("à");
        expect(a).toBe(false);
    });
    // Fails condiitons 3
    it("tests for negative validation of name with alpha and non-alpha special characters, test 1", function() {
        var a = validName("S@M");
        expect(a).toBe(false);
    });
    // Fails conditions 3
    it("tests for negative validation of name with non-alpha special characters, test 2", function() {
        var a = validName("Samantha Réy");
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
    */

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


    /* !!!!!!!! NOTE: This test was removed from the suite as it was incorrect !!!!!!
     * !!!!!!!!  given the equirements of host addresses                       !!!!!!
    // Fails condition 5
    it("tests for negative validation of two '-' characters in a row", function() {
        var a = validHost("abcdefg.--.abcdefg");
        expect(a).toBe(false);
    });
    */


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


    /* !!!! NOTE: validEmail("ABCDEFG.HIJKLMNOPQRSTUVWXYZ") was changed to
     * !!!! validEmail(ABCDEFG@H.IJKLMNOPQRSTUVWXYZ) as
     * !!!! "ABCDEFG.HIJKLMNOPQRSTUVWXYZ" is not a valid email format and the purpose
     * !!!! of the test was to get positive validation on a correctly formatted email
     * !!!! with all the uppercase characters
     */
    it("tests for positive validation of all allowed uppercase alpha characters in input", function() {
        var a = validEmail("ABCDEFG@H.IJKLMNOPQRSTUVWXYZ");
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



/* !!!! ----------------- VALIDATION TESTS FOR MILESTONE 4A ----------------- !!!! */
describe("Test for validation of password", function() {

    // Valid password
    /* 1. Must not be empty
       2. Must have between 6 and 64 characters
       3. Must contain at least one capital letter
       5. Must contain at least one number character
       4. May contain lower and uppercase letters, numbers, and the special characters
            ! @ # $ %  ^ & * ( ) - _ = + / ? ' ;
    */

    /* Postitive Validation Tests*/
    it("tests for positive validation of valid password", function() {
        var a = validPass("pAssw0rd");
        expect(a).toBe(true);
    });
    it("tests for validation of all valid letters, upper and lowercase, and numbers",
    function() {
        var a = validPass("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789");
        expect(a).toBe(true);
    });
    it("tests for validation of all valid special characters",
    function() {
        var a = validPass("A1!@#$%^&*()-_=+/?';");
        expect(a).toBe(true);
    });
    it("tests for valid 6 character password", function() {
        var a = validPass("Abcd3f");
        expect(a).toBe(true);
    });
    it("tests for valid 64 character password", function() {
        var a = validPass("Correcthorsebatterystaplecorrecthorsebatterystaplecorrecthorse12");
        expect(a).toBe(true);
    });

    /* Negative Validation Tests */
    // Fails condition 1
    it("tests for negative validation of empty input", function() {
        var a = validPass(null);
        expect(a).toBe(false);
    });
    // Fails conditions 1 and 2
    it("tests for negative validation of 0 character input", function() {
        var a = validPass("");
        expect(a).toBe(false);
    });
    // Fails condition 2
    it("tests for negative validation of 5 character input ", function() {
        var a = validPass("Abc12");
        expect(a).toBe(false);
    });
    // Fails condition 2
    it("tests for negative validation of 65 character input ", function() {
        var a = validPass("Correcthorsebatterystaplecorrecthorsebatterystaplecorrecthorse123");
        expect(a).toBe(false);
    });
    // Fails condition 3
    it("tests for negative validation of no capital letter in input", function() {
        var a = validPass("samrey1");
        expect(a).toBe(false);
    });
    // Fails condition 4
    it("tests for negative validation of no number in input", function() {
        var a = validPass("samrey");
        expect(a).toBe(false);
    });
    /// Fails condition 5
    it("tests for negative validation of special characters in input", function() {
        var a = validPass("samRey1<");
        expect(a).toBe(false);
    });
    
});

describe("Test for validation of numeric inputs", function() {

    // Valid number
    /* 1. Must not be empty
       2. Must contain only number characters
    */

    /* Postitive Validation Tests*/
    it("tests for valid number input", function() {
        var a = isNumeric("00");
        expect(a).toBe(true);
    });
    it("tests for valid number input where number is greater than 0", function() {
        var a = isNumeric("1");
        expect(a).toBe(true);
    });

    /* Negative Validation Tests */
    // Fails condition 1
    it("tests for negative validation of empty input", function() {
        var a = isNumeric(null);
        expect(a).toBe(false);
    });
    // Fails condition 1
    it("tests for negative validation of 0 character input", function() {
        var a = isNumeric("");
        expect(a).toBe(false);
    });
    // Fails condition 2
    it("tests for negative validation of non-numeric input with alpha characters", function() {
        var a = isNumeric("111a")
        expect(a).toBe(false);
    });
    // Fails condition 2
    it("tests for negative validation of non-numeric inpute with special characters", function() {
        var a = isNumeric("100.10");
        expect(a).toBe(false);
    });
    
});

describe("Test for validation of monetary number inputs", function() {

    // Valid monetary input
    /* 1. Must not be empty
       2. Must contain only number characters and at most 1 '.' character
       3. If input contains a '.', then there must be two number characters
            after the '.'
    */

    /* Postitive Validation Tests*/
    it("tests for valid monetary input without decimal", function() {
        var a = isNumeric("100");
        expect(a).toBe(true);
    });
    it("tests for valid number input where number is greater than 0 without decimal", function() {
        var a = isNumeric("100");
        expect(a).toBe(true);
    });
    /* Postitive Validation Tests*/
    it("tests for valid monetary input with decimal", function() {
        var a = isNumeric(".00");
        expect(a).toBe(true);
    });
    it("tests for valid number input where number is greater than 0 with decimal", function() {
        var a = isNumeric("99.55");
        expect(a).toBe(true);
    });

    /* Negative Validation Tests */
    // Fails condition 1
    it("tests for negative validation of empty input", function() {
        var a = isNumeric(null);
        expect(a).toBe(false);
    });
    // Fails condition 1
    it("tests for negative validation of 0 character input", function() {
        var a = isNumeric("");
        expect(a).toBe(false);
    });
    // Fails condition 2
    it("tests for negative validation of non-numeric input with alpha characters", function() {
        var a = isNumeric("a")
        expect(a).toBe(false);
    });
    // Fails condition 2
    it("tests for negative validation of non-numeric inpute with special characters", function() {
        var a = isNumeric("!");
        expect(a).toBe(false);
    });
    // Fails condition 2
    it("tests for negative validation of non-numeric inpute with more than one decimal", function() {
        var a = isNumeric("101.11.12");
        expect(a).toBe(false);
    });
    // Fails condition 3
    it("tests for negative validation of invalid decimal placement, test 1", function() {
        var a = isNumeric(".1");
        expect(a).toBe(false);
    });
    // Fails condition 3
    it("tests for negative validation of invalid decimal placement, test 2", function() {
        var a = isNumeric(".");
        expect(a).toBe(false);
    });
    // Fails condition 3
    it("tests for negative validation of invalid decimal placement, test 3", function() {
        var a = isNumeric(".123");
        expect(a).toBe(false);
    });
    // Fails condition 3
    it("tests for negative validation of invalid decimal placement, test 4", function() {
        var a = isNumeric("10.1");
        expect(a).toBe(false);
    });
    // Fails condition 3
    it("tests for negative validation of invalid decimal placement, test 5", function() {
        var a = isNumeric("10.");
        expect(a).toBe(false);
    });
    // Fails condition 3
    it("tests for negative validation of invalid decimal placement, test 6", function() {
        var a = isNumeric("10.123");
        expect(a).toBe(false);
    });
    
});
