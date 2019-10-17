$(document).ready(function () {

    function print_again() {
        $("#result").append("<p>Not ready!</p>");
    }

    function call_answer(result) {
        // document.getElementById("result").innerHTML = result.status
        // $("#result").append( "<p>Test</p>" );
        var count = 0;

        while (count < 3) {
            setTimeout(function () {

                // if (result.status != 'SUCCESS') {
                    // document.getElementById("result").innerHTML = 'Not finished yet';
                    // setTimeout('print_again()', 1);
                    // $("#result").append( "<p>Please wait!</p>" )
                    $("#result").append("<p>Not ready!</p>")
                // }
                count++;

            }, 3000);
        }

        // $.ajax({
        //     url: '/show_result/'+ task_id,
        //     type: 'GET',
        //
        //     }
        //
        // )
    }

    function make_request(text, method = "post") {
        $.ajax({
            url: '/call_task',
            type: 'POST',
            // data: {
            //     email: 'email@example.com',
            //     message: text
            // },
            success: function (msg) {
                response_task = msg;
                call_answer(response_task);
            },
            // async: false,
        });
        // document.getElementById("result").innerHTML = "wait for a while!"

        // document.getElementById("result").innerHTML = prediction
        // change_prediction_result(prediction);
    }

    window.onload = function () {
        document.getElementById("send").onclick = function () {
            // mock_make_request(essay_text);
            // $("#result").append(" testing!")
            make_request();
            // var element = document.getElementById("div1");
        }
    }

});




