// https://docs.cypress.io/api/introduction/api.html

describe("My First Test", () => {
  it("register", () => {
    cy.visit("http://localhost:8080/signup");
    cy.get("input")
      .eq(0)
      .type("adamparke1");
    cy.get("input")
      .eq(1)
      .type("adamparke1@gmail.com");
    cy.get("input")
      .eq(2)
      .type("Boston1991");
    cy.get("input")
      .eq(3)
      .type("Boston1991");
    cy.get("input")
      .eq(4)
      .type("adam");
    cy.get("input")
      .eq(5)
      .type("Park");
    cy.get("input")
      .eq(6)
      .type("567374845");
    cy.get("input")
      .eq(7)
      .type("Przylaszczkowa 5f{enter}");
    cy.wait(400);
    cy.get("button")
      .contains("Register")
      .click();
    cy.wait(400);
  });
  it("login", () => {
    cy.visit("http://localhost:8080/login");
    cy.contains("Login");
    cy.get("#input-24").type("adamparke1");
    cy.get("#input-28").type("Boston1991");
    cy.server();
    cy.route("POST", "/api/auth/login").as("login");
    cy.get("button").click();
    cy.wait(["@login"]);
    cy.wait(1500);
  });

  it("cashin", () => {
    cy.get("a")
      .eq(2)
      .click();

    cy.wait(1000);
    cy.get("input")
      .eq(2)
      .clear();
    cy.get("input")
      .eq(0)
      .type("EUR{enter}");
    cy.get("input")
      .eq(2)
      .type(60);
    cy.get("button")
      .contains("Cash in")
      .click();
    cy.wait(500);
    cy.contains("60.00 EUR");
  });
  it("money transfer", () => {
    cy.get("a")
      .eq(2)
      .click();
    cy.wait(200);

    cy.get("div.v-list-item__title")
      .contains("Transfer")
      .parent()
      .click();
    cy.get("input")
      .eq(0)
      .type("macikoj3");
    cy.get("div.v-select__selections").click();
    cy.get("div.v-list-item__title")
      .contains("EUR")
      .click();
    cy.get("input")
      .eq(3)
      .type("15");
    cy.get("input")
      .eq(4)
      .type("tytul");
    cy.get("button")
      .contains("Commit transfer")
      .click();
    cy.wait(1000);
  });

  it("currency conversion", () => {
    cy.get("a")
      .eq(2)
      .click();
    cy.wait(200);

    cy.get("div.v-list-item__title")
      .contains("Currency conversion")
      .parent()
      .click();
    cy.wait(200);
    cy.get("input")
      .eq(0)
      .type("EUR");
    cy.get("input")
      .eq(3)
      .type("PLN");
    cy.get("input")
      .eq(2)
      .clear();
    cy.get("input")
      .eq(2)
      .type("1{enter}");
    cy.wait(200);
    cy.get("button")
      .contains("Change currency")
      .click();
    cy.wait(600);
    cy.get("div.v-list-item__title")
      .contains("Your currencies")
      .parent()
      .click();
    cy.wait(600);
    cy.contains("PLN");
  });
  it("profile history", () => {
    cy.get("a")
      .eq(3)
      .click();
    cy.wait(500);
    cy.contains("Money transfer");
    cy.contains("Currency exchange");
  });
});
