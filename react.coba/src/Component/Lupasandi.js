import { LockOutlined, UserOutlined } from '@ant-design/icons';
import { Button, Form, Input, Card } from 'antd';
import React from 'react';

const Login = () => {
  const onFinish = (values) => {
    console.log('Received values of form: ', values);
  };

  return (
    <div style={{padding: "300px", background: '#ececec'}}>
        <Card
        style={{width: 300, height: 250}}
        >
        <Form className='card' name="normal_login" initialValues={{
            remember: true,
        }} onFinish={onFinish} >

            <h1>Forgot Password</h1>

        <Form.Item name="username" rules={[
            {
                required: true,
                message: 'Please input your Username!',
            },
            ]}
        >
            <Input prefix={<UserOutlined className="site-form-item-icon" />} placeholder="Username" />
        </Form.Item>
        <Form.Item name="password" rules={[
            {
                required: true,
                message: 'Please input your Password!',
            },
            ]}
        >
            <Input prefix={<LockOutlined className="site-form-item-icon" />}
            type="password" placeholder="Password" />
            
        </Form.Item>

        <Form.Item>
            <Button type="primary" htmlType="submit" className="login-form-button">
            Kirim
            </Button>
        </Form.Item>
        </Form>
        </Card>
    </div> 
  );
};

export default Login;
