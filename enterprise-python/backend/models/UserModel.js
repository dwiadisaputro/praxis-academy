import { Sequelize } from "sequelize";
import db from "../config/Database.js"

const {DataTypes} = Sequelize;

const User = db.define('users', {
    name: DataTypes.STRING,
    email: DataTypes.String,
    gender: DataTypes.STRING
})