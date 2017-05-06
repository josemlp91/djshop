$(document).ready(function(){

    $("#id_price_type").change(function(){
        var price_type = $(this).val();
        if(price_type == "price_per_serving"){
            $(".field-container-id_serving_size").show();
            $(".field-container-id_min_serving_size").show();
            $(".field-container-id_max_serving_size").show();
        }else{
            $("#id_serving_size").val("");
            $(".field-container-id_serving_size").hide();
            $(".field-container-id_min_serving_size input").val("");
            $(".field-container-id_min_serving_size").hide();
            $(".field-container-id_max_serving_size input").val("");
            $(".field-container-id_max_serving_size").hide();
        }
    });

    $("#id_price_type").change();

});