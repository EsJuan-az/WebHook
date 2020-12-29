
$(document).ready(() => {
    $(".submitHook").click(() => {
        try{
            new URL($("#id_url").val())
        }catch{
            alert("Your URL is not valid")
            $("#id_url").val("")
            return 0
        }
        $(".ctn-form-page form").trigger("submit")
        
    })
})