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
    $.ajax({
        url: "/testbootstrap/?pageno="+pageno,
    }).done(function(response) {
    });
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
        $("#property").html(create_base_page());
});

