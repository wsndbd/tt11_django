$(document).ready(function() {
    var pageno = parseInt($("#input_page").val());
    console.log("response$(document).ready(function() { ", pageno);
    $.ajax({
        url: "/goods_content/?pageno=" + pageno,
    }).done(function(response) {
        console.log("response ", response);
        $("#div_goods_content").html(response);
    });
});

