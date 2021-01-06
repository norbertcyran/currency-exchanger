// https://docs.cypress.io/api/introduction/api.html

describe("My First Test", () => {
  it("login",() => {
    cy.visit("http://localhost:8080/login");
    cy.contains("Login");
    cy.get("#input-24").type("macikoj2");
    cy.get("#input-28").type("aaaaaaaa2");
    cy.server()
    cy.route('POST', '/api/auth/login').as('login');
    cy.get('button').click()
    cy.wait(['@login']);
    cy.wait(1500)

  });
  it("cashin",() => {
    cy.get('a').eq(3).click()
    cy.get('a').eq(2).click()
    // cy.get('div.v-card__title').contains("EU").parent().within(()=>{
    //   cy.get('button').click()
    // })
    // cy.wait(100)
    // cy.get('input').clear()
    // cy.get('input').type('40')
    // cy.get('button').contains("Add").click()
    // cy.wait(1000)

  });
});