

print = console.log;

class Shape {

	
	_halfAngle = 180;

	_get_area(){
		throw new Error('You have to implement the method _get_area');
	}
	_get_perimeter(){
		throw new Error('You have to implement the method _get_perimeter');
	}
	_get_str(){
		throw new Error('You have to implement the method _get_str');
	}


	check_value(...value){
		for (var i = 0; i < value.length; i++){

			if (typeof(value[i]) == 'number'){
				if (value[i] < 0) throw "less than 0";
			}
			else { throw "Must be Number" }
		}
		return true;
	}

}

class Circle extends Shape {

		constructor(radius) {
		super();
		this.check_value(radius);
		this._r = radius;
	} 
	
	_get_area = () => Math.round(Math.PI*this._r**2);

	_get_perimeter = () => Math.round(2*Math.PI*this._r);

	_get_str = () => {
		return `Circle radius = ${this._r}cm`
		
	}
	
	get radius() {
		return this._r;
	}

	set radius(value) {

		this._r = this.check_value(value);
	}

	#method() {
		console.log(this._halfAngle);
		

	}

	getMethod() {
		return this.#method();
	}
	
}
 
class Triangle extends Shape{
	

	constructor(a, b, c) {
		super();
		this.check_value(a,b,c);
		this._a = a;
		this._b = b;
		this._c = c;
		this.sum  = this._a + this._b + this._c;

	} 
	
	_get_area = () => {
		var s = this.sum / 2;
		return Math.round(Math.sqrt(s*(s-this._a)*(s-this._b)*(s-this._c)));
	};

	_get_perimeter = () => Math.round(this.sum);
	
	_get_str = () => `Triangle a=${this._a}cm, b=${this._b}cm, c=${this._c}cm`;


}



class EquilateralTriangle extends Triangle{

	constructor(a){
		super(a,a,a);
	}

	_get_str = () => `EquilateralTriangle a=${this._a}cm`;

}


class Rectangle extends Shape{
	

	constructor(a, b) {
		super();
		this.check_value(a,b);
		this._a = a;
		this._b = b;
		this.sum  = this._a + this._b;

	} 
	
	_get_area = () => {
		
		return Math.round(this._a * this._b);
	};

	_get_perimeter = () => Math.round(2*this._a + 2*this._b);
	
	_get_str = () => `Rectangle a=${this._a}cm, b=${this._b}cm`;


}



class Square extends Rectangle{

	constructor(a){
		super(a,a);
	}

	

	_get_str = () => `Square a=${this._a}cm`;

}
class ShapeList {

	constructor(){
		this.shapes = [];
	}

	add_shape=(shape)=>{
		if(shape instanceof Shape){
			this.shapes.push(shape);
		}
		else throw TypeError;
	}

	_get_str = () => `ShapeList ${this.shapes}`

	get_large_shape_perimeter=()=>{

		var xx = new Map();
		var i = [];
	    this.shapes.forEach((x)=>xx.set(x._get_perimeter(), x._get_str()));

		for (let x of xx.keys()){
			i.push(x);
		}
		
		let ii = [];
		for (let x of i){
			ii.push(x);
		}

		for (let y=0;y<ii.length-1;y++){
			for(let x = y+1;x<ii.length;x++){
				if (ii[y]>ii[x]){
					var tmp = ii[y];
					ii[y]=ii[x];
					ii[x]=tmp;
			}
		}
		}
		ii.reverse();		
		return `MAX PERIMETER=${ii[0]}cm ${xx.get(ii[0])}`;
	}

	get_large_shape_area=()=>{
		var xx = new Map();
		var i = [];
	    this.shapes.forEach((x)=>xx.set(x._get_area(), x._get_str()));

		for (let x of xx.keys()){
			i.push(x);
		}
		
		let ii = [];
		for (let x of i){
			ii.push(x);
		}

		for (let y=0;y<ii.length-1;y++){
			for(let x = y+1;x<ii.length;x++){
				if (ii[y]>ii[x]){
					var tmp = ii[y];
					ii[y]=ii[x];
					ii[x]=tmp;
			}
		}
		}
		ii.reverse();
		
		return `MAX AREA=${ii[0]}cm ${xx.get(ii[0])}`;
	}

}




// MAIN
main = () =>{
	const v = new ShapeList();
	v.add_shape(new Circle(50));
	v.add_shape(new Circle(90));
	v.add_shape(new Triangle(550,650,880));

	print(v.shapes);
	print(v.get_large_shape_perimeter());
	print(v.get_large_shape_area());
}


main();




module.exports = Circle, Triangle, Square, ShapeList;