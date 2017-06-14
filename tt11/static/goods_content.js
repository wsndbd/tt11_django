function reload_special_case_list_next_page() {
    var username = $("#specialcase_list_form_username").val();
    var state = $("#specialcase_list_form_state").val();
    var pageno = parseInt($("#specialcase_list_form_pageno").val()) + 1;
    $.ajax({
        url: "/c/specialcase/list/?username="+username+"&state="+state+"&pageno="+pageno,
    }).done(function(response) {
        $("#property").html(create_list_case_page(response));
    });
}

function reload_special_case_list_last_page() {
    var pageno = parseInt($("#specialcase_list_form_pageno").val()) - 1;
    window.navigate("/testbootstrap/?pageno="+pageno);
    /*
    $.ajax({
        url: "/testbootstrap/?pageno="+pageno,
    }).done(function(response) {
    });
    */
}

function reload_special_case_list() {
    var username = $("#specialcase_list_form_username").val();
    var state = $("#specialcase_list_form_state").val();
    var pageno = $("#specialcase_list_form_pageno").val();

    $.ajax({
        url: "/c/specialcase/list/?username="+username+"&state="+state+"&pageno="+pageno,
    }).done(function(response) {
        $("#property").html(create_list_case_page(response));
    });
}

$(document).ready(function() {
    var pageno = parseInt($("#input_page").val()) - 1;
    console.log("response$(document).ready(function() { ", pageno);
    $.ajax({
        url: "/goods_content/?pageno=" + pageno,
    }).done(function(response) {
        console.log("response ", response);
        $("#div_goods_content").html(response);
    });
});

