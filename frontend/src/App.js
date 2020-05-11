import React, { Component } from 'react';
import './App.css';
import Login from './components/Login'
import { BrowserRouter as Router, Route, Switch, Redirect } from 'react-router-dom';
import Home from './components/Home';
import { TopNav } from './components/Nav'
import Me from './components/Me'
import { login } from './components/constants/urls'
import Author from './components/Author';
import Post from './components/Post';
import CreatePost from './components/CreatePost';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      authenticated: localStorage.getItem('token') ? true : false,
    };
    this.handleLogin = this.handleLogin.bind(this);
    this.Logout = this.Logout.bind(this);
  }

  handleLogin = (event, data) => {
    event.preventDefault();
    fetch(login, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
      .then(res => res.json())
      .then(json => {
        localStorage.setItem('token', json.token);
        localStorage.setItem('user_id', json.user.id);
        localStorage.setItem('user_email', json.user.email);
        localStorage.setItem('user_name', json.user.name);
        this.setState({
          logged_in: true
        });
      }).catch((err) => {
        console.log(err);
      });

  }

  Logout = () => {
    localStorage.clear();
    this.setState({
      logged_in: false
    });
    return (<Redirect to="/login" />);
  };

  render() {
    return (<>
      <Router>
        <TopNav authenticated={this.state.authenticated} />
        {/* A <Switch> looks through its children <Route>s and
      renders the first one that matches the current URL. */}
        <Switch>
          <Route exact path="/login">
            <Login handleLogin={this.handleLogin} />
          </Route>
          <Route exact path="/logout" >
            <this.Logout handleLogout={this.handleLogout} />
          </Route>
          <Route exact path="/home">
            <Home />
          </Route>
          <Route exact path="/me">
            <Me />
          </Route>
          <Route exact path="/createpost">
            <CreatePost />
          </Route>
          <Route exact path="/author/:id" component={Author} />
          <Route exact path="/post/:id" component={Post} />
        </Switch>
      </Router>
    </>
    );
  }
}

export default App;
