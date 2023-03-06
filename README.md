# <p align="center">One bot to rule them all
**Telegram bot solution for bringing automated home controls even closer to user**

## Purpose
Main purpose of this project is to demonstrate the possibilities of integrating home control systems with wide-spread messengers such as Telegram. The following example implements advanced user management system which may be useful for temporarily sharing controls with users with different levels of access. Such feature may be implemented as a intuitive and easy to access home control system for rented apartments and hotels.

## Why telegram?
In course of last couple years Telegram user base has been growing steeply which made telegram a perfect choice for uniting various systems in one app which is free and already installed on a user device. One more advantage of using telegram as a remote controller for your home devices is vast amount of solutions for constructing a bot which come with a huge variety of plugins which improve user experience and manage bot effectively.

## Is it safe?
Yes! The bot settings can be controlled exclusively by the admin. Users are stored in database and may be removed on check-in and check-out.

## Which may be controlled?
Basically anything. This project is divided into several parts which include:
* Camera and image processing with opencv
* Direct controls of wifi-enabled controllers such as ESP32
* Communication with commercial home-automation systems which are already installed in apartment

## Building blocks
The system may consist of various elements, but the core is always a central server on which bot is running. If the system is applied in a single apartment single board computers may be used (such as raspberry pi). Further elements of the system depend on the needs of homeowner.
  


## Bot structure
```bash
├───bin                 # some bath scripts for docker
├───bot
│   ├───filters         # aiogram filters
│   ├───handlers
│   │   ├───errors      # error handlers
│   │   └───users       # message handlers
│   ├───keyboards
│   │   ├───default     # aiogram markups
│   │   └───inline      # aiogram inline markups
│   ├───middlewares     # aiogram middlewares
│   └───states          # aiogram states
├───data
│   ├───backups         # database backups
│   │   └───postgres
│   ├───locales         # i18n locales
│   └───logs            # bot logs
├───models              # database models
├───opencv              # opencv server for image processing
├───embedded
│   ├───ESP32           # Hardware based on ESP32 chip
│   ├───STM32           # Hardware based on STM32 chip
│   └───other           # Other hardware
└───services            # database services
```
