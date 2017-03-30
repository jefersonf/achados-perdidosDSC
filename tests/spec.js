describe('Protractor running on Mim Acher App', function() {

	var target = 'http://127.0.0.1:5000/#/home';
	
	beforeEach(function() {
    	browser.get(target);
	    browser.waitForAngular();
  	});
	
	it('should add a new lost item', function() {
    
	    browser.driver.sleep(1000);
	    
	    // Tenta adicionar novo item
	    element(by.id('btn-add')).click();
	    browser.driver.sleep(500);

	    // Marca como achado
	    element(by.id('inlineRadio1')).click();
	    browser.driver.sleep(500);

	    element(by.id('itemTitle')).sendKeys('Fone de Ouvido');
	    browser.driver.sleep(500);

	    element(by.id('itemDescription')).sendKeys('Fone de ouvido branco, marca samsung. Encontrado do dia 25/13/2017 às 15:00 pm dentro do LCC');
	    browser.driver.sleep(500);

	    element(by.id('curUserEmail')).sendKeys('jefersonnpn@gmail.com');
	    browser.driver.sleep(500);

	    element(by.model('filePathName')).sendKeys('/home/jeferson/Pictures/runtime_squi.jpg');
	    browser.driver.sleep(500);

	    element(by.id('addItem')).click();

	    browser.waitForAngular();

	    let list = element.all(by.css('#perdidos .portlet-header'));
	    expect(list.count()).toBe(1);
	});

	it('should add a new found item', function() {

	    browser.driver.sleep(1000);
	    
	    // Tenta adicionar novo item
	    element(by.id('btn-add')).click();
	    browser.driver.sleep(500);

	    // Marca como achado
	    element(by.id('inlineRadio2')).click();
	    browser.driver.sleep(500);

	    element(by.id('itemTitle')).sendKeys('Casaco Preto');
	    browser.driver.sleep(500);

	    element(by.id('itemDescription')).sendKeys('Casaco Preto. Encontrado do dia 23/13/2017 às 11:00 a.m. no LCC');
	    browser.driver.sleep(500);

	    element(by.id('curUserEmail')).sendKeys('jefersonnpn@gmail.com');
	    browser.driver.sleep(500);

	    element(by.model('filePathName')).sendKeys('/home/jeferson/Pictures/runtime_squi.jpg');
	    browser.driver.sleep(500);

	    element(by.id('addItem')).click();

	    browser.waitForAngular();

	    let list = element.all(by.css('#achados .portlet-header'));
	    expect(list.count()).toBe(1);

	});

});
