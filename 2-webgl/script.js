var scene;
var camera;
var renderer;

var cylinder;
var stopped = false;

$(document).ready(function(){
    setup();
    addCylinder();
    addLight();
    render();
});


function setup() {
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera( 45, window.innerWidth / window.innerHeight, 1, 1000 );

    camera.position.z = 700;

    renderer = new THREE.WebGLRenderer();
    renderer.setSize( window.innerWidth, window.innerHeight );
    document.body.appendChild( renderer.domElement );
}

function addLight() {
    var ambientLight = new THREE.AmbientLight(0x222222);
    scene.add(ambientLight);

    var directionalLight = new THREE.DirectionalLight(0xffffff);
    directionalLight.position.set(1, 1, 1).normalize();
    scene.add(directionalLight);
}

function addCylinder() {
    cylinder = new THREE.Mesh(
        new THREE.CylinderGeometry(
            100,
            100,
            400,
            50,
            50,
            false),
        new THREE.MeshPhongMaterial({
            // light
            specular: '#a9fcff',
            // intermediate
            color: '#00abb1',
            // dark
            emissive: '#006063',
            shininess: 100
        }));
    cylinder.overdraw = true;
    scene.add( cylinder );
}

function stop(){
    stopped = true;
}

function start() {
    stopped = false;
    render();
}

function render() {
    cylinder.rotation.x += 0.05;
    cylinder.rotation.z += 0.1;
    renderer.render( scene, camera );
    if(stopped !== true) {
        requestAnimationFrame( render );
    } else {
        console.log("stopped");
    }
}
