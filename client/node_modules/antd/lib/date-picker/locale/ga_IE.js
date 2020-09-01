"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = void 0;

var _ga_IE = _interopRequireDefault(require("rc-picker/lib/locale/ga_IE"));

var _ga_IE2 = _interopRequireDefault(require("../../time-picker/locale/ga_IE"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

function _extends() { _extends = Object.assign || function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; }; return _extends.apply(this, arguments); }

// Merge into a locale object
var locale = {
  lang: _extends({
    placeholder: 'Roghnaigh dáta',
    yearPlaceholder: 'Roghnaigh bliain',
    quarterPlaceholder: 'Roghnaigh ráithe',
    monthPlaceholder: 'Roghnaigh mí',
    weekPlaceholder: 'Roghnaigh seachtain',
    rangePlaceholder: ['Dáta tosaigh', 'Dáta deiridh'],
    rangeYearPlaceholder: ['Tús na bliana', 'Deireadh na bliana'],
    rangeMonthPlaceholder: ['Tosaigh mhí', 'Deireadh mhí'],
    rangeWeekPlaceholder: ['Tosaigh an tseachtain', 'Deireadh na seachtaine']
  }, _ga_IE["default"]),
  timePickerLocale: _extends({}, _ga_IE2["default"])
}; // All settings at:
// https://github.com/ant-design/ant-design/blob/master/components/date-picker/locale/example.json

var _default = locale;
exports["default"] = _default;