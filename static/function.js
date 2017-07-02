function start_game() {
    my_area.start();

}

var my_area = {
    canvas : document.getElementById("tic_tac_toe_canvas"),
    start : function(){
        this.canvas.width = 410;
        this.canvas.height = 410;
        this.context = this.canvas.getContext("2d");
        this.horizontal_bar1 = new bar(400, 10, "black",5, 130);
        this.horizontal_bar2 = new bar(400, 10, "black",5, 260);
        this.vertical_bar1 = new bar(10, 400, "black",130, 5);
        this.vertical_bar2 = new bar(10, 400, "black",260, 5);
        this.plays = [];
        this.turn = 1;
        this.filling = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];
        this.canvas.addEventListener('click', function(event) {
            var x = event.pageX;
            var y = event.pageY;
            positions = area(x, y);
            updateGameArea(positions[0], positions[1]);
        });
    },
    clear : function(){
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
        this.horizontal_bar1 = new bar(400, 10, "black",5, 130);
        this.horizontal_bar2 = new bar(400, 10, "black",5, 260);
        this.vertical_bar1 = new bar(10, 400, "black",130, 5);
        this.vertical_bar2 = new bar(10, 400, "black",260, 5);
        this.plays = [];
        this.turn = 1;
        this.filling = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];
    }
}

function area(x, y){
    var areax = Math.ceil(x/130);
    var areay = Math.ceil(y/130);
    return [areax, areay];
}

function bar(width, height, color, x, y){
    this.width = width;
    this.height = height;
    ctx = my_area.context;
    ctx.fillStyle = color;
    this.x = x;
    this.y = y;
    ctx.fillRect(this.x, this.y, this.width, this.height);
}

function updateGameArea(px, py){
    turn = my_area.turn;
    if(my_area.filling[px-1][py-1] == 0){
        my_area.filling[px-1][py-1] = turn;
        if(turn == 1){
            my_area.plays.push(new Cross(px, py));
            my_area.turn = 2;
        }
        else{
            my_area.plays.push(new Circle(px, py));
            my_area.turn = 1;
        }
    }
    var winner = victory(px, py);
    if(winner != 0){
        setTimeout(function(){
        alert("Player " + turn+ " has won the game!")
        my_area.clear();

    }, 20);
    }
    else{
        var i = 0;
        var draw = true;
        while(i < 3){
            if(my_area.filling[i].includes(0)){
                draw = false;
            }
            i++;
        }
        if(draw){
            setTimeout(function(){
                alert("Draw!");
                my_area.clear();
            }, 10);
        }
    }
}

function victory(px, py){
    var i = 0;
    vertical_victory = my_area.filling[px-1][0] != 0 && my_area.filling[px-1][0] == my_area.filling[px-1][1] && my_area.filling[px-1][1] == my_area.filling[px-1][2];
    horizontal_victory = my_area.filling[0][py-1] != 0 && my_area.filling[0][py-1] == my_area.filling[1][py-1] && my_area.filling[1][py-1] == my_area.filling[2][py-1];
    diagonal_victory1 = false;
    diagonal_victory2 = false;
    if(px == py){
        if(px == 2){
            diagonal_victory1 = my_area.filling[0][0] == my_area.filling[1][1] && my_area.filling[1][1] == my_area.filling[2][2];
            diagonal_victory2 = my_area.filling[0][2] == my_area.filling[1][1] && my_area.filling[1][1] == my_area.filling[2][0];
        }
        else{
            diagonal_victory1 = my_area.filling[0][0] == my_area.filling[1][1] && my_area.filling[1][1] == my_area.filling[2][2];
        }
    }
    else if(px + py == 4){
        diagonal_victory2 = my_area.filling[0][2] == my_area.filling[1][1] && my_area.filling[1][1] == my_area.filling[2][0];
    }
    if(horizontal_victory){
        WinLine(5, 65+(135*(py-1)), 405, 65+(135*(py-1)));
    }
    else if(vertical_victory){
        WinLine(65+(135*(px-1)), 5, 65+(135*(px-1)), 405);
    }
    else if(diagonal_victory1){
        WinLine(5, 5, 405, 405);
    }
    else if(diagonal_victory2){
        WinLine(405, 5, 5, 405);
    }
    else{
        return false;
    }
    return true;
}

function WinLine(startx, starty, endx, endy){
    ctx = my_area.context;
    ctx.beginPath();
    ctx.lineWidth = 2;
    ctx.strokeStyle = "black";
    ctx.moveTo(startx, starty);
    ctx.lineTo(endx, endy);
    ctx.stroke();
    ctx.closePath();
}


function Cross(px, py){
    x = 65+ (135*(px-1));
    y = 65+ (135*(py-1));
    ctx = my_area.context;

    ctx.beginPath();
    ctx.moveTo(x - 55, y - 55);
    ctx.lineTo(x + 55, y + 55);
    ctx.lineWidth = 10;
    ctx.strokeStyle = "blue";
    ctx.stroke();
    ctx.moveTo(x + 55, y - 55);
    ctx.lineTo(x - 55, y + 55);
    ctx.stroke();
    ctx.closePath();
}


function Circle(px, py){
    ctx = my_area.context;
    ctx.beginPath();
    ctx.arc(65 + (135*(px-1)),65+(135*(py-1)),55,0,2.0*Math.PI);
    ctx.lineWidth = 10;
    ctx.strokeStyle = "red";
    ctx.stroke();
    ctx.closePath();
}

start_game();