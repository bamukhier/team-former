
$(document).ready(function(){
  eel.getTeams()(showOutput);

  $("#exportBtn").click(function(){
    eel.exportData()(notifyCreation);
  });

});


function showOutput(generatedTeams){
    
    for (let i=0; i<generatedTeams.length; i++){
        var cardHTML = ''
        let openCardHTML = `<div class="card" style=""><div class="card-block"><h4 class="card-title" style="text-align: center; font-weight: bold">Team ${i+1}</h4><ul>`
        cardHTML += openCardHTML;
        //   $("#output-cards").append(openCardHTML)
        for (let j=0; j<generatedTeams[i].length; j++){
            let teamMember = `<li style="font-size: 20px">${generatedTeams[i][j]}</li>`
            cardHTML += teamMember;
           // $("#output-cards").append(teamMember)
        }
        let closeCardHTML = `</ul></div></div>`;
        cardHTML += closeCardHTML;
        $("#output-cards").append(cardHTML);
    }
}

function notifyCreation(){
    alert('created "Generated-Teams.txt" in the same application directory.')
}
