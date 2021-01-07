// https://docs.cypress.io/api/introduction/api.html

describe("My First Test", () => {
  // it("login",() => {
  //   cy.visit("http://localhost:8080/login");
  //   cy.contains("Login");
  //   cy.get("#input-24").type("macikoj3");
  //   cy.get("#input-28").type("aaaaaaaa3");
  //   cy.server()
  //   cy.route('POST', '/api/auth/login').as('login');
  //   cy.get('button').click()
  //   cy.wait(['@login']);
  //   cy.wait(1500)

  // });
  // it("cashin",() => {
  //   cy.get('a').eq(2).click()
  //   // cy.get('div.v-card__title').contains("EU").parent().within(()=>{
  //   //   cy.get('button').click()
  //   // })
  //   cy.wait(1000)
  //   cy.get('input').eq(2).clear()
  //   cy.get("input").eq(0).type("EUR{enter}");
  //   cy.get("input").eq(2).type(30)
  //   cy.get('button').contains("Cash in").click()
  //   cy.wait(1000)
  //   cy.contains("60.00 EUR")

  // });
  it('register',()=>{
    cy.visit("http://localhost:8080/signup");
    cy.get('input').eq(0).type("macikoj4")
    cy.get('input').eq(1).type("macikoj4@gmail.com")
    cy.get('input').eq(2).type("aaaaaaaa4")
    cy.get('input').eq(3).type("aaaaaaaa4")
    cy.get('input').eq(4).type("adam")
    cy.get('input').eq(5).type("Park")
    cy.get('input').eq(6).type("567374845")
    cy.get('input').eq(7).type("Przylaszczkowa 5f")
    cy.get("button").contains("Register").click()
  })
});