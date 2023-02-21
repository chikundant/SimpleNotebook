window.onload=function(){
    input_body = document.getElementsByClassName('scope_body')[0]
    current_count_of_words = document.getElementsByClassName('current_count')[0]

    scope_title = document.getElementsByClassName('scope_title')[0]

    let count;
    let MAX_COUNT_LETTERS_BODY = 250
    let MAX_COUNT_LETTERS_TITLE = 30

    count = input_body.value.length
    current_count_of_words.innerHTML = count

    input_body.addEventListener("input", function(){
        count = input_body.value.length
        if (count > MAX_COUNT_LETTERS_BODY){
            input_body.value = input_body.value.slice(0, 250)
            current_count_of_words.innerHTML = 250
        }
        else{
            current_count_of_words.innerHTML = count
        }
    });

    scope_title.addEventListener("input", function(){
        console.log(scope_title.value.length)
        if (scope_title.value.length >= MAX_COUNT_LETTERS_TITLE){
            scope_title.value = scope_title.value.slice(0, MAX_COUNT_LETTERS_TITLE)
        }
    })
}

