//npm init
//Jest test npm i jest --save-dev   && edit pacakge.json "test":"jest"
//npm test

var Circle = require("./my_code_oop");
var Triangle = require("./my_code_oop");
var Square = require("./my_code_oop");
var ShapeList =  require("./my_code_oop");


const sq = new Square(6);
const cc = new Circle(5);
const tr = new Triangle(5,7,8);
const sl = new ShapeList(1);//must be empty arg

	test('check constructor Circle', ()=>{
		expect(cc._r).toBe(5);
	});

	test('check _get_area Circle', ()=>{
		expect(cc._get_area()).toBe(79);
	});

	test('check value Circle', ()=>{
		expect(()=>new Circle(-5)).toThrow();
	});

	test('check _get_area Circle', ()=>{
		expect(cc._get_perimeter()).toBe(31);
	});
		
	test('check value Triangle', ()=>{
		expect(()=>new Triangle(-5,0,9)).toThrow();
	});

	test('check perimeter Triangle', ()=>{
		expect(tr._get_perimeter()).toBe(31);
	});

	test('check value Square', ()=>{
		expect(()=>new Square(-9)).toThrow();
	});

	test('check _get_area Square(6)', ()=>{
		expect(sq._get_area()).toBe(113);
	});


