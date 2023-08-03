class Ducktypium {
    calibrationSequence = []
    constructor(color) {
        this.color = color;
        if (color != "red" && color != "blue" && color != "yellow"){
            throw 'Error!';
        }
        return this.color
    } 
    refract(string){
        if (string != "red" && string != "blue" && string != "yellow"){
            throw 'Error!';
        }
        else if (string == this.color){
            return string;
        }
        else if ((string == "red" && this.color == "blue") || (string == "blue" && this.color == "red")){
            return String("purple");
        }
        else if ((string == "red" && this.color == "yellow") || (string == "yellow" && this.color == "red")){
            return String("orange");
        }
        else if ((string = "yellow" && this.color == "blue") || (string = "blue" && this.color == "yellow")){
            return String("green");
        }
    }
    calibrate(array){
        array.sort((a,b) => a-b);
        array.forEach((el) => {
            el = el*3
            this.calibrationSequence.push(el)
        })
        
    }
}