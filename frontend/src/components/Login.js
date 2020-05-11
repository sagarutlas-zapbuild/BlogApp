import React from 'react'
import { Redirect } from 'react-router-dom'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'
import { Component } from 'react';

class Login extends Component {
    constructor(props) {
        super(props);
        this.state = {
            username: '',
            password: ''
        };

        this.handleChange = this.handleChange.bind(this);
    }
    handleChange = (event) => {
        this.setState({
            [event.target.name]: event.target.value,
        });
    }
    render() {
        if (localStorage.getItem('token') ? true : false) {
            return (<Redirect to='/home' />);
        }
        else {
            return (<div >
                <Form className="APP" name="loginform" onSubmit={(event) => { this.props.handleLogin(event, this.state); }}>
                    <Form.Row>

                        <Form.Label>Email</Form.Label>

                        <Form.Control type="email" name="email" onChange={(event) => { this.handleChange(event); }}></Form.Control>

                    </Form.Row>
                    <Form.Row>

                        <Form.Label>Password</Form.Label>


                        <Form.Control type="password" name="password" onChange={(event) => { this.handleChange(event); }}></Form.Control>

                    </Form.Row>
                    <Form.Row>
                        <Button type="submit" variant="primary">Login</Button>
                    </Form.Row>

                </Form>
            </div>);
        }
    }
}

export default Login