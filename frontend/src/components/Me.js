import React from 'react'
import { rawUser } from './constants/rawdata'
import Form from 'react-bootstrap/Form';
import Col from 'react-bootstrap/Col';
import { Component } from 'react';
import { user } from './constants/urls';

class Me extends Component {
    constructor(props) {
        super(props);
        this.state = rawUser;
    }

    componentDidMount() {
        fetch(user(localStorage.getItem('user_id')), {
            method: 'GET',
        })
            .then(res => {
                return res.json();
            })
            .then((data) => {
                this.setState(data);
            }).catch((error) => console.log(error));
    }

    render() {
        return (<Form>
            <Form.Row>
                <Form.Group as={Col}>
                    <Form.Label>
                        Name
            </Form.Label>
                    <Form.Control type="text" />
                </Form.Group>
                <Form.Group as={Col}>
                    <Form.Label>
                        Email
            </Form.Label>
                    <Form.Control type="email" />
                </Form.Group>
            </Form.Row>
            <Form.Group as={Col}>
                <Form.Label>
                    Intro
        </Form.Label>
                <Form.Control as='textarea' />
            </Form.Group>
        </Form>)
    }

}
export default Me
