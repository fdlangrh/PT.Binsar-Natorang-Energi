function posting() {
    let title = $("#image-title").val();
    if (!title) {
        return alert("post title cannot be empty");
    }
    let content = $("#image-description").val();

    if (!content) {
        return alert("post description cannot be empty");
    }

    let file = $("#image").prop("files")[0];


    let form_data = new FormData();

    form_data.append("file_give", file);
    form_data.append("title_give", title);
    form_data.append("content_give", content);

    $.ajax({
        type: "POST",
        url: "/upload",
        data: form_data,
        contentType: false,
        processData: false,
        success: function (response) {
            console.log(response);
            alert(response.msg)
            window.location.reload();
        },
    });
}

// function edit() {
//   let title = $("#input-title-edit").val();
//   let newImage = $("#input-file-edit")[0].files[0];
//   let layout = $("#layout-select-edit").val();

//   let formData = new FormData();
//   formData.append("title", title);
//   formData.append("layout", layout);

//   if (newImage) {
//     formData.append("file_give", newImage);
//   }


//   $.ajax({
//       type:'POST',
//       url:'/edit',
//       data:{
//           title_give:title,
//           content_give:content,
//           file_give:newImage,
//           id_give:id

//       },
//       success:function(response){
//           alert(response.msg)
//           window.location.href = 'data.html'
//       }
//   })
// }

function baru(){
        let id = $('#_id').val();
       
        let title = $("#image-title").val();
        let content = $("#image-description").val();
        let file = $("#image").prop("files")[0];


        let form_data = new FormData();

    form_data.append("file_give", file);
    form_data.append("title_give", title);
    form_data.append("content_give", content);
    form_data.append("id_give", id);

    $.ajax({
        type: "POST",
        url: "/baru",
        data: form_data,
        contentType: false,
        processData: false,
        success: function (response) {
            alert(response.msg)
            window.location.href = '/data'  
          },
        });
        
}

function update(num) {
    $.ajax({
      type: "GET",
      url: `/edit/update/${num}`,
      success: function (response) {
        if (response.result === "success") {
          let post = response.post;
          $("#image-title").val(post.title);
          // $("#_id").val(post.id)
          $("#image-description").val(post.content);

          $("#edit-post-button").attr("onclick", `save(${num})`);
          $("#exampleModal").modal("show");
        } else {
          alert(response.msg);
        }
      },
    });
  }

  function save(num) {
    let title = $("#image-title").val();
    let newImage = $("#image")[0].files[-1];
    let content = $("#image-description").val();
    let id =$("#_id").val();
  
    let formData = new FormData();
    formData.append("_id", id);
    formData.append("title", title);
    formData.append("content", content);
  
    if (newImage) {
      formData.append("file_give", newImage);
    }
  
    $.ajax({
      type: "POST",
      url: `/data/edit/${num}`,
      data: formData,
      contentType: false,
      processData: false,
      success: function (response) {
        if (response.result === "success") {
          window.location.href = '/data'
        } else {
          alert(response.msg);
        }
      },
    });
  }