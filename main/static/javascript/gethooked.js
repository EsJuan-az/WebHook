function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}
$(document).ready(() => {
    $(".boton.gethooked").click(() => {
        $(".ctn-display").fadeOut()
        console.log("Clicked")
        $(".ctn-gethookedRandom img").css("transform","rotate(1080deg)")
                                     .css("transition","all 5s")
        setTimeout(() => {
           $(".ctn-gethookedRandom img").css("transform","none") 
           let page = pages[getRandomInt(0,pages.length)]
            $(".ctn-display").text("The name of this page is " + page.name + "... Enjoy!")
            $(".ctn-display").fadeIn()
            setTimeout(() => {window.open(page.url)},1000)
        },5500)
    })

})