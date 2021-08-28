$(document).ready(function(){
    $("#addBtn").click(function(){
        var stdName = $("#std-name").val();
        var stdGpa = $("#std-gpa").val();
        var stdSkill = $('input[name="skill"]:checked').val();
        var skillText = $('input[name="skill"]:checked').parent().find('label').text();
        var stdTime = $('input[name="prftime"]:checked').val();
        var timeText = $('input[name="prftime"]:checked').parent().find('label').text();
        if (stdName == '' || stdGpa == '' || stdSkill == null || stdTime == null){
            alert('Input can not be blank');
         } else {
             tableList.push([stdName, stdGpa, skillText, timeText])
             $("#std-name").val("");
             $("#std-gpa").val("");
             $('input[name="skill"]:checked').prop('checked', false);
             $('input[name="prftime"]:checked').prop('checked', false);
             populateTable();
             
         }
    });

    $("#submitBtn").click(function(){
        var fTeamSize = $("#form-team-size").val();
        if (fTeamSize == ''){
            alert('Team Size must be specified.');
        } else {
            $.LoadingOverlay("show", {
                text        : "Team formation will take few moments..."
                        });
            eel.generateTeams(tableList, fTeamSize)(cb)
            window.location.href = "/output.html";
        }
    });

    $("#submitBtn2").click(function(){
        var  importTeamSize = $("#importTeamSize").val();
        var isUploaded = $("#upFile").val();
        if (importTeamSize == ''){
            alert('Team Size must be specified.');
        } else if (isUploaded  == ''){
            alert('A CSV file must be uploaded.');
        }
        else {
            $.LoadingOverlay("show", {
                text        : "Team formation will take few moments..."
            });
            var output = document.getElementById('strOutput').innerHTML;
            eel.readFile(output, importTeamSize)(cb)
            window.location.href = "/output.html";
        }

    });


    $("#upFile").change(function(){
          
        var fr=new FileReader(); 
        fr.onload=function(){ 
            document.getElementById('strOutput') 
                    .textContent=fr.result; 
        } 
          
        fr.readAsText(this.files[0]); 
    })
});
var tableList = []



function populateTable (){
    $("#stdTable").html("<thead><tr><td style='font-weight: bold'>ID</td><td style='font-weight: bold'>Name</td><td style='font-weight: bold'>GPA</td><td style='font-weight: bold'>Skill</td><td style='font-weight: bold'>Timing</td><td style='font-weight: bold'>Action</td></tr></thead>")
    for (let i=0; i<tableList.length; i++){
        var tableRow = `<tr><td>${i+1}</td><td>${tableList[i][0]}</td><td>${tableList[i][1]}</td><td>${tableList[i][2]}</td><td>${tableList[i][3]}</td><td><button type="button" class="btn btn-danger" onclick="remove(${i})">Remove</button></td></tr>`
        $("#stdTable").append(tableRow)
    }
}

function remove(row) {
    tableList.splice(row, 1);
    populateTable()
}

function cb(){
    
    $.LoadingOverlay("hide");
}

