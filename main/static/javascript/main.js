
$(document).ready(() => {
    //Toggles de activar nav
    
    $('.nav-off').click(() => {
        $('.nav-off').hide()
        $('.nav-on').show()
        $('.nav-lateral').animate({
            left:"-300px"
        },500)
    })
    $('.nav-on').click(() => {
        $('.nav-on,.activar-nav img').hide()
        $('.nav-off').show()
        $('.nav-lateral').animate({
            left:"0px"
        },500)
    })
    $(document).click((e) => {
        if(e.target.className != 'nav-on' && e.target.className != 'nav-lateral'){
            $('.nav-on,.activar-nav img').show()
            $('.nav-off').hide()
            $('.nav-lateral').animate({
            left:"-300px"
            },500)
        }
    })
})