function addPreference(selectedPreference){
  var container = $("#field-row-container");
  var text = $("#field-row").text();
  var idn = container.find("[data-id='container']").size() + 1;
  var id = "tercih" + idn
  var body = $(text.format(id, idn));
  body.find("button[data-id='remove']").click(function () {
    $(this).parents("[data-id='container']").remove();
  });
  container.append(body);


  var accomodations={}
  var selectOptions = "";
  $.ajax({
         url : "/accounts/getaccomodations/stu/"+$("#id_gender").val(),
         type : "GET",
         dataType: "json",
         success : function(data) {
                   accomodations=data;
                   $.each(accomodations,function(key,value){
                     selectOptions += "<option value='" + key + "'>" + value + "</option>"
                   });
                   body.find('select').append(selectOptions);
                   if(selectedPreference){
                     body.find('select').val(selectedPreference);
                   }
                   $("#remove").show();
         },
  });
}
function countrychanged(selectbox){
    var country = $(selectbox).val();
    if (country == "TR"){
        $("#id_ykimlikno").parent().parent().find('span').hide();
        $("#id_tckimlikno").parent().parent().find('div').first().append("<span class='required'></span>");
    }else{
        $("#id_tckimlikno").parent().parent().find('span').hide();
        $("#id_ykimlikno").parent().parent().find('div').first().append("<span class='required'></span>");
    }
}

function mobilephonenumberchanged(){
    var mobile = document.getElementById('id_mobilephonenumber').value;
    var filledMobilePhoneNumberCheckbox = document.getElementById("id_filled_mobile_phone_number");
    var EmptyMobilePhoneNumberCheckbox = document.getElementById("id_empty_mobile_phone_number");

    if (mobile.trim() === "") {
        $("#id_filled_mobile_phone_number").parent().parent().find('span').hide();
        $("#id_empty_mobile_phone_number").parent().parent().find('div').first().append("<span class='required'></span>");
        filledMobilePhoneNumberCheckbox.style.display = "none";
        EmptyMobilePhoneNumberCheckbox.style.display = "block";
    } else {
        filledMobilePhoneNumberCheckbox.style.display = "block";
        EmptyMobilePhoneNumberCheckbox.style.display = "none";
        $("#id_empty_mobile_phone_number").parent().parent().find('span').hide();
        $("#id_filled_mobile_phone_number").parent().parent().find('div').first().append("<span class='required'></span>");
    }

}

document.addEventListener("DOMContentLoaded", function () {
    mobile_checkboxes_hide_show();
});

function mobile_checkboxes_hide_show() {
    var mobilePhoneNumberInput = document.getElementById("id_mobilephonenumber");
    var EmptyMobilePhoneNumberCheckbox = document.getElementById("id_empty_mobile_phone_number");
    var filledMobilePhoneNumberCheckbox = document.getElementById("id_filled_mobile_phone_number");

    if (mobilePhoneNumberInput.value.trim() === "") {
        EmptyMobilePhoneNumberCheckbox.style.display = "block";
        filledMobilePhoneNumberCheckbox.style.display = "none";
        $("#id_empty_mobile_phone_number").parent().parent().find('div').first().append("<span class='required'></span>");
    } else {
        EmptyMobilePhoneNumberCheckbox.style.display = "none";
        filledMobilePhoneNumberCheckbox.style.display = "block";
        $("#id_filled_mobile_phone_number").parent().parent().find('div').first().append("<span class='required'></span>");
    }
}


function genderchanged(){
    if($(".accomodations_pref_div select").length){
      $("#field-row-container").html("");
      bootbox.alert("Konaklama Tercihlerinizi Güncelleyiniz", function(){});
      addPreference();
     }
}
$(document).ready(function(){
    $("#id_tckimlikno").parent().parent().find('div').first().append("<span class='required'></span>");
    $('#id_profilephoto').bind('change', function() {
      if (this.files[0].size > 5*1000*1000){
        this.value=null;
        alert("Profil fotografı boyutu 5 MB'yi geçemez");
      }
    });
    $('#id_document').bind('change', function() {
      if (this.files[0].size > 10*1000*1000){
        this.value=null;
        alert("Görevlendirme Belgesi boyutu 10 MB'yi geçemez");
      }
    });
});

