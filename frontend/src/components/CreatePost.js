import React from 'react'
import { Component } from 'react';
import Form from 'react-bootstrap/Form';


class CreatePost extends Component {
    constructor(props) {
        super(props);
        this.state = {
            title: "",
            content: "",
            publish: false,
            summary: ""
        }
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event) {
        this.setState({ [event.target.name]: event.target.value, });
        console.log(this.state);
    }

    render() {
        return (<Form>
            <Form.Group>
                <Form.Label>
                    Title
                </Form.Label>
                <Form.Control type='text' name="title" required value={this.state.title} onChange={(event) => { this.handleChange(event); }} />
            </Form.Group>
            <Form.Group>
                <Form.Label>
                    Summary
                </Form.Label>
                <Form.Control as={'textarea'} name="summary" value={this.state.summary} onChange={(event) => { this.handleChange(event); }} />
            </Form.Group>
            <Form.Group>
                <Form.Label>
                    Content
                </Form.Label>
                <Form.Control as={'textarea'} name="content" value={this.state.content} onChange={(event) => { this.handleChange(event); }} />
            </Form.Group>
            <Form.Check
                name="publish"
                type='switch'
                label="publish"
                id="publish"
                value={this.state.publish}
                onChange={() => { this.setState({ publish: !this.state.publish }); console.log(this.state.publish); }} />

        </Form>)
    }
}

export default CreatePost