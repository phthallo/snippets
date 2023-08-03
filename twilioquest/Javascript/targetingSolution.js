class TargetingSolution {
    constructor(config) {
        this.xcoord = String(config.x);
        this.ycoord = String(config.y);
        this.zcoord = String(config.z);
    }
    target(){
        return ('('+this.xcoord+', '+this.ycoord+', '+this.zcoord+')')
    }
}