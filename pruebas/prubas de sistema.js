'use strict'

/**
*@desc Pruebas de sistema para Webbot API
*@desc Software usado Nodejs, Mocha & Supertest
*@desc instalar Nodejs y luego correr npm install
*
*/


var supertest = require('./node_modules/supertest');
var server = supertest.agent("http://localhost");

describe('Prueba API Webbot', function() {
		it('/get/id=1 Resultado esperado: correcta', function(done) {
			server
			.get('/get/id=1/')
			.set('Accept', 'application/json')
			.expect(200)
        	.end((err, res) => {
				if(err) return done(err);
				if(res.body.numFound <= 0 || typeof res.body.numFound !== 'number'){
					throw  'Incorrecto'
				}
				done()
			})
		});
		it('/get/id=TRUE Resultado esperado: incorrecta', function(done) {
			server
			.get('/get/id=TRUE/')
			.set('Accept', 'application/json')
			.expect(200)
        	.end((err, res) => {
				if(err) return done(err);
				if(res.body.numFound <= 0 || typeof res.body.numFound !== 'number'){
					throw  'Incorrecto'
				}
				done()
			})
		});
		it('/get/id=FALSE Resultado esperado: incorrecta', function(done) {
			server
			.get('/get/id=FALSE/')
			.set('Accept', 'application/json')
			.expect(200)
        	.end((err, res) => {
				if(err) return done(err);
				if(res.body.numFound <= 0 || typeof res.body.numFound !== 'number'){
					throw  'Incorrecto'
				}
				done()
			})
		});
		it('/get/id=213ADAOISJD Resultado esperado: incorrecta', function(done) {
			server
			.get('/get/id=213ADAOISJD/')
			.set('Accept', 'application/json')
			.expect(200)
        	.end((err, res) => {
				if(err) return done(err);
				if(res.body.numFound <= 0 || typeof res.body.numFound !== 'number'){
					throw  'Incorrecto'
				}
				done()
			})
		});
		it('/get/list Resultado esperado: correcta', function(done) {
			server
			.get('/get/list/')
			.set('Accept', 'application/json')
			.expect(200)
        	.end((err, res) => {
				if(err) return done(err);
				if(res.body.numFound <= 0 || typeof res.body.numFound !== 'number'){
					throw  'Incorrecto'
				}
				done()
			})
		});
		it('/get/list=1 Resultado esperado: incorrecta', function(done) {
			server
			.get('/get/list=1/')
			.set('Accept', 'application/json')
			.expect(200)
        	.end((err, res) => {
				if(err) return done(err);
				if(res.body.numFound <= 0 || typeof res.body.numFound !== 'number'){
					throw  'Incorrecto'
				}
				done()
			})
		});
		it('/get/autor=Sergio Resultado esperado: correcta', function(done) {
			server
			.get('/get/autor=Sergio/')
			.set('Accept', 'application/json')
			.expect(200)
        	.end((err, res) => {
				if(err) return done(err);
				if(res.body.numFound <= 0 || typeof res.body.numFound !== 'number'){
					throw  'Incorrecto'
				}
				done()
			})
		});
		it('/get/autor={} Resultado esperado: incorrecta', function(done) {
			server
			.get('/get/autor={}/')
			.set('Accept', 'application/json')
			.expect(200)
        	.end((err, res) => {
				if(err) return done(err);
				if(res.body.numFound <= 0 || typeof res.body.numFound !== 'number'){
					throw  'Incorrecto'
				}
				done()
			})
		});
		it('/get/autor=TRUE Resultado esperado: incorrecta', function(done) {
			server
			.get('/get/autor=TRUE/')
			.set('Accept', 'application/json')
			.expect(200)
        	.end((err, res) => {
				if(err) return done(err);
				if(res.body.numFound <= 0 || typeof res.body.numFound !== 'number'){
					throw  'Incorrecto'
				}
				done()
			})
		});
		it('/get/titulo=Plant Resultado esperado: correcta', function(done) {
			server
			.get('/get/titulo=Plant/')
			.set('Accept', 'application/json')
			.expect(200)
        	.end((err, res) => {
				if(err) return done(err);
				if(res.body.numFound <= 0 || typeof res.body.numFound !== 'number'){
					throw  'Incorrecto'
				}
				done()
			})
		});
		it('/get/titulo=TRUE Resultado esperado: incorrecta', function(done) {
			server
			.get('/get/titulo=TRUE/')
			.set('Accept', 'application/json')
			.expect(200)
        	.end((err, res) => {
				if(err) return done(err);
				if(res.body.numFound <= 0 || typeof res.body.numFound !== 'number'){
					throw  'Incorrecto'
				}
				done()
			})
		});
		it('/get/url= Resultado esperado: correcta', function(done) {
			server
			.get('/get/url=/')
			.set('Accept', 'application/json')
			.expect(200)
        	.end((err, res) => {
				if(err) return done(err);
				if(res.body.numFound <= 0 || typeof res.body.numFound !== 'number'){
					throw  'Incorrecto'
				}
				done()
			})
		});
		it('/get/url= Resultado esperado: incorrecta', function(done) {
			server
			.get('/get/url=/')
			.set('Accept', 'application/json')
			.expect(200)
        	.end((err, res) => {
				if(err) return done(err);
				if(res.body.numFound <= 0 || typeof res.body.numFound !== 'number'){
					throw  'Incorrecto'
				}
				done()
			})
		});
		it('/get/isbn= Resultado esperado: correcta', function(done) {
			server
			.get('/get/isbn=/')
			.set('Accept', 'application/json')
			.expect(200)
        	.end((err, res) => {
				if(err) return done(err);
				if(res.body.numFound <= 0 || typeof res.body.numFound !== 'number'){
					throw  'Incorrecto'
				}
				done()
			})
		});
		it('/get/isbn= Resultado esperado: incorrecta', function(done) {
			server
			.get('/get/isbn=/')
			.set('Accept', 'application/json')
			.expect(200)
        	.end((err, res) => {
				if(err) return done(err);
				if(res.body.numFound <= 0 || typeof res.body.numFound !== 'number'){
					throw  'Incorrecto'
				}
				done()
			})
		});
		it('/get/anio=2010 Resultado esperado: correcta', function(done) {
			server
			.get('/get/anio=2010/')
			.set('Accept', 'application/json')
			.expect(200)
        	.end((err, res) => {
				if(err) return done(err);
				if(res.body.numFound <= 0 || typeof res.body.numFound !== 'number'){
					throw  'Incorrecto'
				}
				done()
			})
		});
		it('/get/anio=2080 Resultado esperado: incorrecta', function(done) {
			server
			.get('/get/anio=2080/')
			.set('Accept', 'application/json')
			.expect(200)
        	.end((err, res) => {
				if(err) return done(err);
				if(res.body.numFound <= 0 || typeof res.body.numFound !== 'number'){
					throw  'Incorrecto'
				}
				done()
			})
		});

	});