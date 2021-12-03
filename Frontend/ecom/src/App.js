import "./App.css";
import { HomePage } from "./containers/HomePage";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import { CustomerAccessPage } from "./containers/customerAccessPage";
import Products from "./components/Products/Products";
import Test from "./components/Products/Test";
import SingleProduct from "./components/Products/Product/SingleProduct";
//import  CheckOutPage  from "./containers/CheckOutPage/CheckOutPage";
//import CartProvider from "./contexts/cart";
//import CheckoutProvider from "./contexts/checkout";
//import CheckoutPage from "../src/pages/checkout";
import React from "react";
//import { BrowserRouter as Router, Switch } from "react-router-dom";
import CommonProvider from "./contexts/common";
import ProductsProvider from "./contexts/products";
import CartProvider from "./contexts/cart";
import CheckoutProvider from "./contexts/checkout";
import AuthLayout from "./layouts/AuthLayout";
import CommonLayout from "./layouts/CommonLayout";
import AuthPage from "./pages/auth";
//import HomePage from "../pages/home";
import CheckoutPage from "./pages/checkout";
import Upload from "./components/Upload";
import "./assets/scss/style.scss";

const App = () => {
  return (
    <div className="App">
      <CommonProvider>
        <ProductsProvider>
          <CartProvider>
            <CheckoutProvider>
              <Router>
                <Switch>
                  <Route
                    path="/"
                    exact
                    component={HomePage}
                    layout={CommonLayout}
                  />
                  <Route
                    path="/checkout"
                    component={CheckoutPage}
                    layout={CommonLayout}
                  />
                  <Route
                    path="/auth"
                    component={AuthPage}
                    layout={AuthLayout}
                  />
                  <Route
                    path="/upload"
                    component={Upload}
                  />
                </Switch>
              </Router>
            </CheckoutProvider>
          </CartProvider>
        </ProductsProvider>
      </CommonProvider>
        
    </div>
  );
}

export default App;
