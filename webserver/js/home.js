var IN_SHURUFA = false;

document.addEventListener('compositionstart', function() {
    IN_SHURUFA = true;
});

document.addEventListener('compositionend', function() {
    IN_SHURUFA = false;
});

function stringToHex(str) {
    const encoder = new TextEncoder();
    const bytes = encoder.encode(str);
    let hex = '';
    for (let byte of bytes) {
        hex += byte.toString(16).padStart(2, '0');
    }
    return hex;
}

window.addEventListener('DOMContentLoaded', function() {
    var input_area = document.getElementById('input-area');
    var input_textbox = document.querySelector('#input-area > div > input');
    var go_img = document.querySelector('#input-area > div > img');
    input_textbox.addEventListener('focusin', function() {
        input_area.classList.add('focusin');
    });
    input_textbox.addEventListener('focusout', function() {
        input_area.classList.remove('focusin');
    });
    input_textbox.addEventListener('input', function() {
        if(input_textbox.value === '') {
            go_img.classList.add('invalid');
        } else {
            go_img.classList.remove('invalid');
        }
    });

    function send_msg() {
        if (input_textbox.value === '') {
            return;
        }
        var data = stringToHex(input_textbox.value);
        window.location.href = '/html/ai_chat.html#' + data;
    }

    go_img.addEventListener('click', send_msg);
    input_textbox.addEventListener('keydown', function(event) {
        if (IN_SHURUFA) {
            return;
        }
        if(event.key === 'Enter') {
            send_msg();
        }
    });
});


