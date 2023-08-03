const life = Number(process.argv[2]);
const dry = Number(process.argv[3]);
if ( 
    life == 0 &&
    dry > 10
) {
    console.log('WATER');
}