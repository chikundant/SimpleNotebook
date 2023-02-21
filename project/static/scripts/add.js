window.onload=function(){
    input_body = document.getElementsByClassName('body')[0]
    input_title = document.getElementsByClassName('title')[0]

    current_count_of_words = document.getElementsByClassName('current_count_of_words')[0]

    let count;
    let MAX_COUNT_LETTERS_BODY = 250
    let MAX_COUNT_LETTERS_TITLE = 30

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
    
    input_title.addEventListener("input", function(){
        console.log(input_title.value.length)
        if (input_title.value.length >= MAX_COUNT_LETTERS_TITLE){
            input_title.value = input_title.value.slice(0, MAX_COUNT_LETTERS_TITLE)
        }
    })


}

