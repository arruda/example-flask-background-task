$(document).ready(function () {
    var timer = null;

    function show_result(result_task_id) {
        $.ajax({
            url: '/show_result/' + result_task_id,
            type: 'GET',
            success: function (msg) {
                response_task = msg;

                document.getElementById("test_result").innerHTML = response_task.status;
                if (response_task.status == 'SUCCESS') {
                    clearInterval(timer);
                    document.getElementById("result").innerHTML = "The answer is " + response_task.content;
                    return;
                }
            },
        });
    }

    function call_answer(result_id) {
        // $("#result").append( "<p>Test</p>" );
        // document.getElementById("result").innerHTML = 'Not ready, please wait ' + count;


        timer = setInterval(function () {
                show_result(result_id);
            },
            1000)

    }


    function make_request(text, method = "post") {
        $.ajax({
            url: '/call_task',
            type: 'POST',
            data: JSON.stringify({
                message: text
            }),
            contentType: 'application/json',
            processData: false,
            success: function (msg) {
                response_task = msg;
                call_answer(response_task.result_task_id);

            },
        });
    };


    document.getElementById("send").onclick = function () {
        essay_text = document.getElementById("essayArea").value;
        make_request(essay_text);
        // var element = document.getElementById("div1");
    }
    // window.onload = function () {
    // }
});




