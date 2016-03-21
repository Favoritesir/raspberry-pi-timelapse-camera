$(".btn-danger").click(function(event) {
  image_to_delete = $(this).parent(".thumbnail").data("image");

  $.post("image/delete/", {image: image_to_delete})
  .done(function(data) {
    console.log(data);
  });

  $(this).parent(".thumbnail").fadeOut();
});
