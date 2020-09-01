(function webpackUniversalModuleDefinition(root, factory) {
	if(typeof exports === 'object' && typeof module === 'object')
		module.exports = factory(require("react"));
	else if(typeof define === 'function' && define.amd)
		define(["react"], factory);
	else if(typeof exports === 'object')
		exports["rc-input-number"] = factory(require("react"));
	else
		root["rc-input-number"] = factory(root["React"]);
})(typeof self !== 'undefined' ? self : this, function(__WEBPACK_EXTERNAL_MODULE_2__) {
return /******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, {
/******/ 				configurable: false,
/******/ 				enumerable: true,
/******/ 				get: getter
/******/ 			});
/******/ 		}
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ (function(module, exports, __webpack_require__) {

__webpack_require__(1);
module.exports = __webpack_require__(5);


/***/ }),
/* 1 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react__ = __webpack_require__(2);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_react__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_classnames__ = __webpack_require__(3);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_classnames___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1_classnames__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_rc_util_es_KeyCode__ = __webpack_require__(4);
var _extends = Object.assign || function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; };

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

function _objectWithoutProperties(obj, keys) { var target = {}; for (var i in obj) { if (keys.indexOf(i) >= 0) continue; if (!Object.prototype.hasOwnProperty.call(obj, i)) continue; target[i] = obj[i]; } return target; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

/* eslint-disable react/prop-types */




function noop() {}

function preventDefault(e) {
  e.preventDefault();
}

function defaultParser(input) {
  return input.replace(/[^\w.-]+/g, '');
}

/**
 * When click and hold on a button - the speed of auto changin the value.
 */
var SPEED = 200;

/**
 * When click and hold on a button - the delay before auto changin the value.
 */
var DELAY = 600;

/**
 * Max Safe Integer -- on IE this is not available, so manually set the number in that case.
 * The reason this is used, instead of Infinity is because numbers above the MSI are unstable
 */
var MAX_SAFE_INTEGER = Number.MAX_SAFE_INTEGER || Math.pow(2, 53) - 1;

var isValidProps = function isValidProps(value) {
  return value !== undefined && value !== null;
};

var isEqual = function isEqual(oldValue, newValue) {
  return newValue === oldValue || typeof newValue === 'number' && typeof oldValue === 'number' && isNaN(newValue) && isNaN(oldValue);
};

var InputNumber = function (_React$Component) {
  _inherits(InputNumber, _React$Component);

  function InputNumber(props) {
    _classCallCheck(this, InputNumber);

    var _this = _possibleConstructorReturn(this, (InputNumber.__proto__ || Object.getPrototypeOf(InputNumber)).call(this, props));

    _initialiseProps.call(_this);

    var value = void 0;
    if ('value' in props) {
      value = props.value;
    } else {
      value = props.defaultValue;
    }
    _this.state = {
      focused: props.autoFocus
    };
    var validValue = _this.getValidValue(_this.toNumber(value));
    _this.state = _extends({}, _this.state, {
      inputValue: _this.toPrecisionAsStep(validValue),
      value: validValue
    });
    return _this;
  }

  _createClass(InputNumber, [{
    key: 'componentDidMount',
    value: function componentDidMount() {
      this.componentDidUpdate();
    }
  }, {
    key: 'componentDidUpdate',
    value: function componentDidUpdate(prevProps) {
      var _props = this.props,
          value = _props.value,
          onChange = _props.onChange,
          max = _props.max,
          min = _props.min;
      var focused = this.state.focused;

      // Don't trigger in componentDidMount

      if (prevProps) {
        if (!isEqual(prevProps.value, value) || !isEqual(prevProps.max, max) || !isEqual(prevProps.min, min)) {
          var validValue = focused ? value : this.getValidValue(value);
          var nextInputValue = void 0;
          if (this.pressingUpOrDown) {
            nextInputValue = validValue;
          } else if (this.inputting) {
            nextInputValue = this.rawInput;
          } else {
            nextInputValue = this.toPrecisionAsStep(validValue);
          }
          this.setState({ // eslint-disable-line
            value: validValue,
            inputValue: nextInputValue
          });
        }

        // Trigger onChange when max or min change
        // https://github.com/ant-design/ant-design/issues/11574
        var nextValue = 'value' in this.props ? value : this.state.value;
        // ref: null < 20 === true
        // https://github.com/ant-design/ant-design/issues/14277
        if ('max' in this.props && prevProps.max !== max && typeof nextValue === 'number' && nextValue > max && onChange) {
          onChange(max);
        }
        if ('min' in this.props && prevProps.min !== min && typeof nextValue === 'number' && nextValue < min && onChange) {
          onChange(min);
        }
      }

      // Restore cursor
      try {
        // Firefox set the input cursor after it get focused.
        // This caused that if an input didn't init with the selection,
        // set will cause cursor not correct when first focus.
        // Safari will focus input if set selection. We need skip this.
        if (this.cursorStart !== undefined && this.state.focused) {
          // In most cases, the string after cursor is stable.
          // We can move the cursor before it

          if (
          // If not match full str, try to match part of str
          !this.partRestoreByAfter(this.cursorAfter) && this.state.value !== this.props.value) {
            // If not match any of then, let's just keep the position
            // TODO: Logic should not reach here, need check if happens
            var pos = this.cursorStart + 1;

            // If not have last string, just position to the end
            if (!this.cursorAfter) {
              pos = this.input.value.length;
            } else if (this.lastKeyCode === __WEBPACK_IMPORTED_MODULE_2_rc_util_es_KeyCode__["a" /* default */].BACKSPACE) {
              pos = this.cursorStart - 1;
            } else if (this.lastKeyCode === __WEBPACK_IMPORTED_MODULE_2_rc_util_es_KeyCode__["a" /* default */].DELETE) {
              pos = this.cursorStart;
            }
            this.fixCaret(pos, pos);
          } else if (this.currentValue === this.input.value) {
            // Handle some special key code
            switch (this.lastKeyCode) {
              case __WEBPACK_IMPORTED_MODULE_2_rc_util_es_KeyCode__["a" /* default */].BACKSPACE:
                this.fixCaret(this.cursorStart - 1, this.cursorStart - 1);
                break;
              case __WEBPACK_IMPORTED_MODULE_2_rc_util_es_KeyCode__["a" /* default */].DELETE:
                this.fixCaret(this.cursorStart + 1, this.cursorStart + 1);
                break;
              default:
              // Do nothing
            }
          }
        }
      } catch (e) {}
      // Do nothing


      // Reset last key
      this.lastKeyCode = null;

      // pressingUpOrDown is true means that someone just click up or down button
      if (!this.pressingUpOrDown) {
        return;
      }
      if (this.props.focusOnUpDown && this.state.focused) {
        if (document.activeElement !== this.input) {
          this.focus();
        }
      }
    }
  }, {
    key: 'componentWillUnmount',
    value: function componentWillUnmount() {
      this.stop();
    }
  }, {
    key: 'getCurrentValidValue',
    value: function getCurrentValidValue(value) {
      var val = value;
      if (val === '') {
        val = '';
      } else if (!this.isNotCompleteNumber(parseFloat(val, 10))) {
        val = this.getValidValue(val);
      } else {
        val = this.state.value;
      }
      return this.toNumber(val);
    }
  }, {
    key: 'getRatio',
    value: function getRatio(e) {
      var ratio = 1;
      if (e.metaKey || e.ctrlKey) {
        ratio = 0.1;
      } else if (e.shiftKey) {
        ratio = 10;
      }
      return ratio;
    }
  }, {
    key: 'getValueFromEvent',
    value: function getValueFromEvent(e) {
      // optimize for chinese input expierence
      // https://github.com/ant-design/ant-design/issues/8196
      var value = e.target.value.trim().replace(/。/g, '.');

      if (isValidProps(this.props.decimalSeparator)) {
        value = value.replace(this.props.decimalSeparator, '.');
      }

      return value;
    }
  }, {
    key: 'getValidValue',
    value: function getValidValue(value) {
      var min = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : this.props.min;
      var max = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : this.props.max;

      var val = parseFloat(value, 10);
      // https://github.com/ant-design/ant-design/issues/7358
      if (isNaN(val)) {
        return value;
      }
      if (val < min) {
        val = min;
      }
      if (val > max) {
        val = max;
      }
      return val;
    }
  }, {
    key: 'setValue',
    value: function setValue(v, callback) {
      // trigger onChange
      var precision = this.props.precision;

      var newValue = this.isNotCompleteNumber(parseFloat(v, 10)) ? null : parseFloat(v, 10);
      var _state = this.state,
          _state$value = _state.value,
          value = _state$value === undefined ? null : _state$value,
          _state$inputValue = _state.inputValue,
          inputValue = _state$inputValue === undefined ? null : _state$inputValue;
      // https://github.com/ant-design/ant-design/issues/7363
      // https://github.com/ant-design/ant-design/issues/16622

      var newValueInString = typeof newValue === 'number' ? newValue.toFixed(precision) : '' + newValue;
      var changed = newValue !== value || newValueInString !== '' + inputValue;
      if (!('value' in this.props)) {
        this.setState({
          value: newValue,
          inputValue: this.toPrecisionAsStep(v)
        }, callback);
      } else {
        // always set input value same as value
        this.setState({
          inputValue: this.toPrecisionAsStep(this.state.value)
        }, callback);
      }
      if (changed) {
        this.props.onChange(newValue);
      }

      return newValue;
    }
  }, {
    key: 'getFullNum',
    value: function getFullNum(num) {
      if (isNaN(num)) {
        return num;
      }
      if (!/e/i.test(String(num))) {
        return num;
      }
      return Number(num).toFixed(18).replace(/\.?0+$/, '');
    }
  }, {
    key: 'getPrecision',
    value: function getPrecision(value) {
      if (isValidProps(this.props.precision)) {
        return this.props.precision;
      }
      var valueString = value.toString();
      if (valueString.indexOf('e-') >= 0) {
        return parseInt(valueString.slice(valueString.indexOf('e-') + 2), 10);
      }
      var precision = 0;
      if (valueString.indexOf('.') >= 0) {
        precision = valueString.length - valueString.indexOf('.') - 1;
      }
      return precision;
    }

    // step={1.0} value={1.51}
    // press +
    // then value should be 2.51, rather than 2.5
    // if this.props.precision is undefined
    // https://github.com/react-component/input-number/issues/39

  }, {
    key: 'getMaxPrecision',
    value: function getMaxPrecision(currentValue) {
      var ratio = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : 1;
      var _props2 = this.props,
          precision = _props2.precision,
          step = _props2.step;

      if (isValidProps(precision)) {
        return precision;
      }
      var ratioPrecision = this.getPrecision(ratio);
      var stepPrecision = this.getPrecision(step);
      var currentValuePrecision = this.getPrecision(currentValue);
      if (!currentValue) {
        return ratioPrecision + stepPrecision;
      }
      return Math.max(currentValuePrecision, ratioPrecision + stepPrecision);
    }
  }, {
    key: 'getPrecisionFactor',
    value: function getPrecisionFactor(currentValue) {
      var ratio = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : 1;

      var precision = this.getMaxPrecision(currentValue, ratio);
      return Math.pow(10, precision);
    }
  }, {
    key: 'fixCaret',
    value: function fixCaret(start, end) {
      if (start === undefined || end === undefined || !this.input || !this.input.value) {
        return;
      }

      try {
        var currentStart = this.input.selectionStart;
        var currentEnd = this.input.selectionEnd;

        if (start !== currentStart || end !== currentEnd) {
          this.input.setSelectionRange(start, end);
        }
      } catch (e) {
        // Fix error in Chrome:
        // Failed to read the 'selectionStart' property from 'HTMLInputElement'
        // http://stackoverflow.com/q/21177489/3040605
      }
    }
  }, {
    key: 'focus',
    value: function focus() {
      this.input.focus();
      this.recordCursorPosition();
    }
  }, {
    key: 'blur',
    value: function blur() {
      this.input.blur();
    }
  }, {
    key: 'select',
    value: function select() {
      this.input.select();
    }
  }, {
    key: 'formatWrapper',
    value: function formatWrapper(num) {
      // http://2ality.com/2012/03/signedzero.html
      // https://github.com/ant-design/ant-design/issues/9439
      if (this.props.formatter) {
        return this.props.formatter(num);
      }
      return num;
    }
  }, {
    key: 'toPrecisionAsStep',
    value: function toPrecisionAsStep(num) {
      if (this.isNotCompleteNumber(num) || num === '') {
        return num;
      }
      var precision = Math.abs(this.getMaxPrecision(num));
      if (!isNaN(precision)) {
        return Number(num).toFixed(precision);
      }
      return num.toString();
    }

    // '1.' '1x' 'xx' '' => are not complete numbers

  }, {
    key: 'isNotCompleteNumber',
    value: function isNotCompleteNumber(num) {
      return isNaN(num) || num === '' || num === null || num && num.toString().indexOf('.') === num.toString().length - 1;
    }
  }, {
    key: 'toNumber',
    value: function toNumber(num) {
      var precision = this.props.precision;
      var focused = this.state.focused;
      // num.length > 16 => This is to prevent input of large numbers

      var numberIsTooLarge = num && num.length > 16 && focused;
      if (this.isNotCompleteNumber(num) || numberIsTooLarge) {
        return num;
      }
      if (isValidProps(precision)) {
        return Math.round(num * Math.pow(10, precision)) / Math.pow(10, precision);
      }
      return Number(num);
    }
  }, {
    key: 'upStep',
    value: function upStep(val, rat) {
      var step = this.props.step;

      var precisionFactor = this.getPrecisionFactor(val, rat);
      var precision = Math.abs(this.getMaxPrecision(val, rat));
      var result = ((precisionFactor * val + precisionFactor * step * rat) / precisionFactor).toFixed(precision);
      return this.toNumber(result);
    }
  }, {
    key: 'downStep',
    value: function downStep(val, rat) {
      var step = this.props.step;

      var precisionFactor = this.getPrecisionFactor(val, rat);
      var precision = Math.abs(this.getMaxPrecision(val, rat));
      var result = ((precisionFactor * val - precisionFactor * step * rat) / precisionFactor).toFixed(precision);
      return this.toNumber(result);
    }
  }, {
    key: 'step',
    value: function step(type, e) {
      var _this2 = this;

      var ratio = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : 1;
      var recursive = arguments[3];

      this.stop();
      if (e) {
        e.persist();
        e.preventDefault();
      }
      var props = this.props;
      if (props.disabled) {
        return;
      }
      var value = this.getCurrentValidValue(this.state.inputValue) || 0;
      if (this.isNotCompleteNumber(value)) {
        return;
      }
      var val = this[type + 'Step'](value, ratio);
      var outOfRange = val > props.max || val < props.min;
      if (val > props.max) {
        val = props.max;
      } else if (val < props.min) {
        val = props.min;
      }
      this.setValue(val);
      this.setState({
        focused: true
      }, function () {
        _this2.pressingUpOrDown = false;
      });
      if (outOfRange) {
        return;
      }
      this.autoStepTimer = setTimeout(function () {
        _this2[type](e, ratio, true);
      }, recursive ? SPEED : DELAY);
    }
  }, {
    key: 'render',
    value: function render() {
      var _classNames;

      var _props3 = this.props,
          prefixCls = _props3.prefixCls,
          disabled = _props3.disabled,
          readOnly = _props3.readOnly,
          useTouch = _props3.useTouch,
          autoComplete = _props3.autoComplete,
          upHandler = _props3.upHandler,
          downHandler = _props3.downHandler,
          className = _props3.className,
          max = _props3.max,
          min = _props3.min,
          style = _props3.style,
          title = _props3.title,
          onMouseEnter = _props3.onMouseEnter,
          onMouseLeave = _props3.onMouseLeave,
          onMouseOver = _props3.onMouseOver,
          onMouseOut = _props3.onMouseOut,
          required = _props3.required,
          onClick = _props3.onClick,
          tabIndex = _props3.tabIndex,
          type = _props3.type,
          placeholder = _props3.placeholder,
          id = _props3.id,
          inputMode = _props3.inputMode,
          pattern = _props3.pattern,
          step = _props3.step,
          maxLength = _props3.maxLength,
          autoFocus = _props3.autoFocus,
          name = _props3.name,
          rest = _objectWithoutProperties(_props3, ['prefixCls', 'disabled', 'readOnly', 'useTouch', 'autoComplete', 'upHandler', 'downHandler', 'className', 'max', 'min', 'style', 'title', 'onMouseEnter', 'onMouseLeave', 'onMouseOver', 'onMouseOut', 'required', 'onClick', 'tabIndex', 'type', 'placeholder', 'id', 'inputMode', 'pattern', 'step', 'maxLength', 'autoFocus', 'name']);

      var _state2 = this.state,
          value = _state2.value,
          focused = _state2.focused;

      var classes = __WEBPACK_IMPORTED_MODULE_1_classnames___default()(prefixCls, (_classNames = {}, _defineProperty(_classNames, className, !!className), _defineProperty(_classNames, prefixCls + '-disabled', disabled), _defineProperty(_classNames, prefixCls + '-focused', focused), _classNames));

      var dataOrAriaAttributeProps = {};
      Object.keys(rest).forEach(function (key) {
        if (key.substr(0, 5) === 'data-' || key.substr(0, 5) === 'aria-' || key === 'role') {
          dataOrAriaAttributeProps[key] = rest[key];
        }
      });

      var editable = !readOnly && !disabled;

      // focus state, show input value
      // unfocus state, show valid value
      var inputDisplayValue = this.getInputDisplayValue();

      var upDisabled = (value || value === 0) && (isNaN(value) || Number(value) >= max);
      var downDisabled = (value || value === 0) && (isNaN(value) || Number(value) <= min);
      var isUpDisabled = upDisabled || disabled || readOnly;
      var isDownDisabled = downDisabled || disabled || readOnly;
      var upClassName = __WEBPACK_IMPORTED_MODULE_1_classnames___default()(prefixCls + '-handler', prefixCls + '-handler-up', _defineProperty({}, prefixCls + '-handler-up-disabled', isUpDisabled));
      var downClassName = __WEBPACK_IMPORTED_MODULE_1_classnames___default()(prefixCls + '-handler', prefixCls + '-handler-down', _defineProperty({}, prefixCls + '-handler-down-disabled', isDownDisabled));

      var upEvents = useTouch ? {
        onTouchStart: isUpDisabled ? noop : this.up,
        onTouchEnd: this.stop
      } : {
        onMouseDown: isUpDisabled ? noop : this.up,
        onMouseUp: this.stop,
        onMouseLeave: this.stop
      };
      var downEvents = useTouch ? {
        onTouchStart: isDownDisabled ? noop : this.down,
        onTouchEnd: this.stop
      } : {
        onMouseDown: isDownDisabled ? noop : this.down,
        onMouseUp: this.stop,
        onMouseLeave: this.stop
      };

      return __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
        'div',
        {
          className: classes,
          style: style,
          title: title,
          onMouseEnter: onMouseEnter,
          onMouseLeave: onMouseLeave,
          onMouseOver: onMouseOver,
          onMouseOut: onMouseOut,
          onFocus: function onFocus() {
            return null;
          },
          onBlur: function onBlur() {
            return null;
          }
        },
        __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
          'div',
          { className: prefixCls + '-handler-wrap' },
          __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
            'span',
            _extends({
              unselectable: 'unselectable'
            }, upEvents, {
              role: 'button',
              'aria-label': 'Increase Value',
              'aria-disabled': isUpDisabled,
              className: upClassName
            }),
            upHandler || __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement('span', {
              unselectable: 'unselectable',
              className: prefixCls + '-handler-up-inner',
              onClick: preventDefault
            })
          ),
          __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
            'span',
            _extends({
              unselectable: 'unselectable'
            }, downEvents, {
              role: 'button',
              'aria-label': 'Decrease Value',
              'aria-disabled': isDownDisabled,
              className: downClassName
            }),
            downHandler || __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement('span', {
              unselectable: 'unselectable',
              className: prefixCls + '-handler-down-inner',
              onClick: preventDefault
            })
          )
        ),
        __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
          'div',
          { className: prefixCls + '-input-wrap' },
          __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement('input', _extends({
            role: 'spinbutton',
            'aria-valuemin': min,
            'aria-valuemax': max,
            'aria-valuenow': value,
            required: required,
            type: type,
            placeholder: placeholder,
            onClick: onClick,
            onMouseUp: this.onMouseUp,
            className: prefixCls + '-input',
            tabIndex: tabIndex,
            autoComplete: autoComplete,
            onFocus: this.onFocus,
            onBlur: this.onBlur,
            onKeyDown: editable ? this.onKeyDown : noop,
            onKeyUp: editable ? this.onKeyUp : noop,
            autoFocus: autoFocus,
            maxLength: maxLength,
            readOnly: readOnly,
            disabled: disabled,
            max: max,
            min: min,
            step: step,
            name: name,
            title: title,
            id: id,
            onChange: this.onChange,
            ref: this.saveInput,
            value: this.getFullNum(inputDisplayValue),
            pattern: pattern,
            inputMode: inputMode
          }, dataOrAriaAttributeProps))
        )
      );
    }
  }]);

  return InputNumber;
}(__WEBPACK_IMPORTED_MODULE_0_react___default.a.Component);

InputNumber.defaultProps = {
  focusOnUpDown: true,
  useTouch: false,
  prefixCls: 'rc-input-number',
  min: -MAX_SAFE_INTEGER,
  step: 1,
  style: {},
  onChange: noop,
  onKeyDown: noop,
  onPressEnter: noop,
  onFocus: noop,
  onBlur: noop,
  parser: defaultParser,
  required: false,
  autoComplete: 'off'
};

var _initialiseProps = function _initialiseProps() {
  var _this3 = this;

  this.onKeyDown = function (e) {
    for (var _len = arguments.length, args = Array(_len > 1 ? _len - 1 : 0), _key = 1; _key < _len; _key++) {
      args[_key - 1] = arguments[_key];
    }

    var _props4 = _this3.props,
        onKeyDown = _props4.onKeyDown,
        onPressEnter = _props4.onPressEnter;


    if (e.keyCode === __WEBPACK_IMPORTED_MODULE_2_rc_util_es_KeyCode__["a" /* default */].UP) {
      var ratio = _this3.getRatio(e);
      _this3.up(e, ratio);
      _this3.stop();
    } else if (e.keyCode === __WEBPACK_IMPORTED_MODULE_2_rc_util_es_KeyCode__["a" /* default */].DOWN) {
      var _ratio = _this3.getRatio(e);
      _this3.down(e, _ratio);
      _this3.stop();
    } else if (e.keyCode === __WEBPACK_IMPORTED_MODULE_2_rc_util_es_KeyCode__["a" /* default */].ENTER && onPressEnter) {
      onPressEnter(e);
    }

    // Trigger user key down
    _this3.recordCursorPosition();
    _this3.lastKeyCode = e.keyCode;
    if (onKeyDown) {
      onKeyDown.apply(undefined, [e].concat(args));
    }
  };

  this.onKeyUp = function (e) {
    for (var _len2 = arguments.length, args = Array(_len2 > 1 ? _len2 - 1 : 0), _key2 = 1; _key2 < _len2; _key2++) {
      args[_key2 - 1] = arguments[_key2];
    }

    var onKeyUp = _this3.props.onKeyUp;


    _this3.stop();

    _this3.recordCursorPosition();

    // Trigger user key up
    if (onKeyUp) {
      onKeyUp.apply(undefined, [e].concat(args));
    }
  };

  this.onChange = function (e) {
    var onChange = _this3.props.onChange;


    if (_this3.state.focused) {
      _this3.inputting = true;
    }
    _this3.rawInput = _this3.props.parser(_this3.getValueFromEvent(e));
    _this3.setState({ inputValue: _this3.rawInput });
    onChange(_this3.toNumber(_this3.rawInput)); // valid number or invalid string
  };

  this.onMouseUp = function () {
    var onMouseUp = _this3.props.onMouseUp;


    _this3.recordCursorPosition();

    if (onMouseUp) {
      onMouseUp.apply(undefined, arguments);
    }
  };

  this.onFocus = function () {
    var _props5;

    _this3.setState({
      focused: true
    });
    (_props5 = _this3.props).onFocus.apply(_props5, arguments);
  };

  this.onBlur = function () {
    var onBlur = _this3.props.onBlur;

    _this3.inputting = false;
    _this3.setState({
      focused: false
    });
    var value = _this3.getCurrentValidValue(_this3.state.inputValue);
    var newValue = _this3.setValue(value);

    if (onBlur) {
      var originValue = _this3.input.value;
      var inputValue = Number(_this3.getInputDisplayValue({ focus: false, value: newValue }));
      _this3.input.value = inputValue;
      onBlur.apply(undefined, arguments);
      _this3.input.value = originValue;
    }
  };

  this.getInputDisplayValue = function (state) {
    var _ref = state || _this3.state,
        focused = _ref.focused,
        inputValue = _ref.inputValue,
        value = _ref.value;

    var inputDisplayValue = void 0;
    if (focused) {
      inputDisplayValue = inputValue;
    } else {
      inputDisplayValue = _this3.toPrecisionAsStep(value);
    }

    if (inputDisplayValue === undefined || inputDisplayValue === null) {
      inputDisplayValue = '';
    }

    var inputDisplayValueFormat = _this3.formatWrapper(inputDisplayValue);
    if (isValidProps(_this3.props.decimalSeparator)) {
      inputDisplayValueFormat = inputDisplayValueFormat.toString().replace('.', _this3.props.decimalSeparator);
    }

    return inputDisplayValueFormat;
  };

  this.recordCursorPosition = function () {
    // Record position
    try {
      _this3.cursorStart = _this3.input.selectionStart;
      _this3.cursorEnd = _this3.input.selectionEnd;
      _this3.currentValue = _this3.input.value;
      _this3.cursorBefore = _this3.input.value.substring(0, _this3.cursorStart);
      _this3.cursorAfter = _this3.input.value.substring(_this3.cursorEnd);
    } catch (e) {
      // Fix error in Chrome:
      // Failed to read the 'selectionStart' property from 'HTMLInputElement'
      // http://stackoverflow.com/q/21177489/3040605
    }
  };

  this.restoreByAfter = function (str) {
    if (str === undefined) return false;

    var fullStr = _this3.input.value;
    var index = fullStr.lastIndexOf(str);

    if (index === -1) return false;

    var prevCursorPos = _this3.cursorBefore.length;
    if (_this3.lastKeyCode === __WEBPACK_IMPORTED_MODULE_2_rc_util_es_KeyCode__["a" /* default */].DELETE && _this3.cursorBefore.charAt(prevCursorPos - 1) === str[0]) {
      _this3.fixCaret(prevCursorPos, prevCursorPos);
      return true;
    }

    if (index + str.length === fullStr.length) {
      _this3.fixCaret(index, index);

      return true;
    }
    return false;
  };

  this.partRestoreByAfter = function (str) {
    if (str === undefined) return false;

    // For loop from full str to the str with last char to map. e.g. 123
    // -> 123
    // -> 23
    // -> 3
    return Array.prototype.some.call(str, function (_, start) {
      var partStr = str.substring(start);

      return _this3.restoreByAfter(partStr);
    });
  };

  this.stop = function () {
    if (_this3.autoStepTimer) {
      clearTimeout(_this3.autoStepTimer);
    }
  };

  this.down = function (e, ratio, recursive) {
    _this3.pressingUpOrDown = true;
    _this3.step('down', e, ratio, recursive);
  };

  this.up = function (e, ratio, recursive) {
    _this3.pressingUpOrDown = true;
    _this3.step('up', e, ratio, recursive);
  };

  this.saveInput = function (node) {
    _this3.input = node;
  };
};

/* harmony default export */ __webpack_exports__["default"] = (InputNumber);

/***/ }),
/* 2 */
/***/ (function(module, exports) {

module.exports = __WEBPACK_EXTERNAL_MODULE_2__;

/***/ }),
/* 3 */
/***/ (function(module, exports, __webpack_require__) {

var __WEBPACK_AMD_DEFINE_ARRAY__, __WEBPACK_AMD_DEFINE_RESULT__;/*!
  Copyright (c) 2017 Jed Watson.
  Licensed under the MIT License (MIT), see
  http://jedwatson.github.io/classnames
*/
/* global define */

(function () {
	'use strict';

	var hasOwn = {}.hasOwnProperty;

	function classNames () {
		var classes = [];

		for (var i = 0; i < arguments.length; i++) {
			var arg = arguments[i];
			if (!arg) continue;

			var argType = typeof arg;

			if (argType === 'string' || argType === 'number') {
				classes.push(arg);
			} else if (Array.isArray(arg) && arg.length) {
				var inner = classNames.apply(null, arg);
				if (inner) {
					classes.push(inner);
				}
			} else if (argType === 'object') {
				for (var key in arg) {
					if (hasOwn.call(arg, key) && arg[key]) {
						classes.push(key);
					}
				}
			}
		}

		return classes.join(' ');
	}

	if (typeof module !== 'undefined' && module.exports) {
		classNames.default = classNames;
		module.exports = classNames;
	} else if (true) {
		// register as 'classnames', consistent with npm package name
		!(__WEBPACK_AMD_DEFINE_ARRAY__ = [], __WEBPACK_AMD_DEFINE_RESULT__ = (function () {
			return classNames;
		}).apply(exports, __WEBPACK_AMD_DEFINE_ARRAY__),
				__WEBPACK_AMD_DEFINE_RESULT__ !== undefined && (module.exports = __WEBPACK_AMD_DEFINE_RESULT__));
	} else {
		window.classNames = classNames;
	}
}());


/***/ }),
/* 4 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/**
 * @ignore
 * some key-codes definition and utils from closure-library
 * @author yiminghe@gmail.com
 */
var KeyCode = {
  /**
   * MAC_ENTER
   */
  MAC_ENTER: 3,

  /**
   * BACKSPACE
   */
  BACKSPACE: 8,

  /**
   * TAB
   */
  TAB: 9,

  /**
   * NUMLOCK on FF/Safari Mac
   */
  NUM_CENTER: 12,

  /**
   * ENTER
   */
  ENTER: 13,

  /**
   * SHIFT
   */
  SHIFT: 16,

  /**
   * CTRL
   */
  CTRL: 17,

  /**
   * ALT
   */
  ALT: 18,

  /**
   * PAUSE
   */
  PAUSE: 19,

  /**
   * CAPS_LOCK
   */
  CAPS_LOCK: 20,

  /**
   * ESC
   */
  ESC: 27,

  /**
   * SPACE
   */
  SPACE: 32,

  /**
   * PAGE_UP
   */
  PAGE_UP: 33,

  /**
   * PAGE_DOWN
   */
  PAGE_DOWN: 34,

  /**
   * END
   */
  END: 35,

  /**
   * HOME
   */
  HOME: 36,

  /**
   * LEFT
   */
  LEFT: 37,

  /**
   * UP
   */
  UP: 38,

  /**
   * RIGHT
   */
  RIGHT: 39,

  /**
   * DOWN
   */
  DOWN: 40,

  /**
   * PRINT_SCREEN
   */
  PRINT_SCREEN: 44,

  /**
   * INSERT
   */
  INSERT: 45,

  /**
   * DELETE
   */
  DELETE: 46,

  /**
   * ZERO
   */
  ZERO: 48,

  /**
   * ONE
   */
  ONE: 49,

  /**
   * TWO
   */
  TWO: 50,

  /**
   * THREE
   */
  THREE: 51,

  /**
   * FOUR
   */
  FOUR: 52,

  /**
   * FIVE
   */
  FIVE: 53,

  /**
   * SIX
   */
  SIX: 54,

  /**
   * SEVEN
   */
  SEVEN: 55,

  /**
   * EIGHT
   */
  EIGHT: 56,

  /**
   * NINE
   */
  NINE: 57,

  /**
   * QUESTION_MARK
   */
  QUESTION_MARK: 63,

  /**
   * A
   */
  A: 65,

  /**
   * B
   */
  B: 66,

  /**
   * C
   */
  C: 67,

  /**
   * D
   */
  D: 68,

  /**
   * E
   */
  E: 69,

  /**
   * F
   */
  F: 70,

  /**
   * G
   */
  G: 71,

  /**
   * H
   */
  H: 72,

  /**
   * I
   */
  I: 73,

  /**
   * J
   */
  J: 74,

  /**
   * K
   */
  K: 75,

  /**
   * L
   */
  L: 76,

  /**
   * M
   */
  M: 77,

  /**
   * N
   */
  N: 78,

  /**
   * O
   */
  O: 79,

  /**
   * P
   */
  P: 80,

  /**
   * Q
   */
  Q: 81,

  /**
   * R
   */
  R: 82,

  /**
   * S
   */
  S: 83,

  /**
   * T
   */
  T: 84,

  /**
   * U
   */
  U: 85,

  /**
   * V
   */
  V: 86,

  /**
   * W
   */
  W: 87,

  /**
   * X
   */
  X: 88,

  /**
   * Y
   */
  Y: 89,

  /**
   * Z
   */
  Z: 90,

  /**
   * META
   */
  META: 91,

  /**
   * WIN_KEY_RIGHT
   */
  WIN_KEY_RIGHT: 92,

  /**
   * CONTEXT_MENU
   */
  CONTEXT_MENU: 93,

  /**
   * NUM_ZERO
   */
  NUM_ZERO: 96,

  /**
   * NUM_ONE
   */
  NUM_ONE: 97,

  /**
   * NUM_TWO
   */
  NUM_TWO: 98,

  /**
   * NUM_THREE
   */
  NUM_THREE: 99,

  /**
   * NUM_FOUR
   */
  NUM_FOUR: 100,

  /**
   * NUM_FIVE
   */
  NUM_FIVE: 101,

  /**
   * NUM_SIX
   */
  NUM_SIX: 102,

  /**
   * NUM_SEVEN
   */
  NUM_SEVEN: 103,

  /**
   * NUM_EIGHT
   */
  NUM_EIGHT: 104,

  /**
   * NUM_NINE
   */
  NUM_NINE: 105,

  /**
   * NUM_MULTIPLY
   */
  NUM_MULTIPLY: 106,

  /**
   * NUM_PLUS
   */
  NUM_PLUS: 107,

  /**
   * NUM_MINUS
   */
  NUM_MINUS: 109,

  /**
   * NUM_PERIOD
   */
  NUM_PERIOD: 110,

  /**
   * NUM_DIVISION
   */
  NUM_DIVISION: 111,

  /**
   * F1
   */
  F1: 112,

  /**
   * F2
   */
  F2: 113,

  /**
   * F3
   */
  F3: 114,

  /**
   * F4
   */
  F4: 115,

  /**
   * F5
   */
  F5: 116,

  /**
   * F6
   */
  F6: 117,

  /**
   * F7
   */
  F7: 118,

  /**
   * F8
   */
  F8: 119,

  /**
   * F9
   */
  F9: 120,

  /**
   * F10
   */
  F10: 121,

  /**
   * F11
   */
  F11: 122,

  /**
   * F12
   */
  F12: 123,

  /**
   * NUMLOCK
   */
  NUMLOCK: 144,

  /**
   * SEMICOLON
   */
  SEMICOLON: 186,

  /**
   * DASH
   */
  DASH: 189,

  /**
   * EQUALS
   */
  EQUALS: 187,

  /**
   * COMMA
   */
  COMMA: 188,

  /**
   * PERIOD
   */
  PERIOD: 190,

  /**
   * SLASH
   */
  SLASH: 191,

  /**
   * APOSTROPHE
   */
  APOSTROPHE: 192,

  /**
   * SINGLE_QUOTE
   */
  SINGLE_QUOTE: 222,

  /**
   * OPEN_SQUARE_BRACKET
   */
  OPEN_SQUARE_BRACKET: 219,

  /**
   * BACKSLASH
   */
  BACKSLASH: 220,

  /**
   * CLOSE_SQUARE_BRACKET
   */
  CLOSE_SQUARE_BRACKET: 221,

  /**
   * WIN_KEY
   */
  WIN_KEY: 224,

  /**
   * MAC_FF_META
   */
  MAC_FF_META: 224,

  /**
   * WIN_IME
   */
  WIN_IME: 229,
  // ======================== Function ========================

  /**
   * whether text and modified key is entered at the same time.
   */
  isTextModifyingKeyEvent: function isTextModifyingKeyEvent(e) {
    var keyCode = e.keyCode;

    if (e.altKey && !e.ctrlKey || e.metaKey || // Function keys don't generate text
    keyCode >= KeyCode.F1 && keyCode <= KeyCode.F12) {
      return false;
    } // The following keys are quite harmless, even in combination with
    // CTRL, ALT or SHIFT.


    switch (keyCode) {
      case KeyCode.ALT:
      case KeyCode.CAPS_LOCK:
      case KeyCode.CONTEXT_MENU:
      case KeyCode.CTRL:
      case KeyCode.DOWN:
      case KeyCode.END:
      case KeyCode.ESC:
      case KeyCode.HOME:
      case KeyCode.INSERT:
      case KeyCode.LEFT:
      case KeyCode.MAC_FF_META:
      case KeyCode.META:
      case KeyCode.NUMLOCK:
      case KeyCode.NUM_CENTER:
      case KeyCode.PAGE_DOWN:
      case KeyCode.PAGE_UP:
      case KeyCode.PAUSE:
      case KeyCode.PRINT_SCREEN:
      case KeyCode.RIGHT:
      case KeyCode.SHIFT:
      case KeyCode.UP:
      case KeyCode.WIN_KEY:
      case KeyCode.WIN_KEY_RIGHT:
        return false;

      default:
        return true;
    }
  },

  /**
   * whether character is entered.
   */
  isCharacterKey: function isCharacterKey(keyCode) {
    if (keyCode >= KeyCode.ZERO && keyCode <= KeyCode.NINE) {
      return true;
    }

    if (keyCode >= KeyCode.NUM_ZERO && keyCode <= KeyCode.NUM_MULTIPLY) {
      return true;
    }

    if (keyCode >= KeyCode.A && keyCode <= KeyCode.Z) {
      return true;
    } // Safari sends zero key code for non-latin characters.


    if (window.navigator.userAgent.indexOf('WebKit') !== -1 && keyCode === 0) {
      return true;
    }

    switch (keyCode) {
      case KeyCode.SPACE:
      case KeyCode.QUESTION_MARK:
      case KeyCode.NUM_PLUS:
      case KeyCode.NUM_MINUS:
      case KeyCode.NUM_PERIOD:
      case KeyCode.NUM_DIVISION:
      case KeyCode.SEMICOLON:
      case KeyCode.DASH:
      case KeyCode.EQUALS:
      case KeyCode.COMMA:
      case KeyCode.PERIOD:
      case KeyCode.SLASH:
      case KeyCode.APOSTROPHE:
      case KeyCode.SINGLE_QUOTE:
      case KeyCode.OPEN_SQUARE_BRACKET:
      case KeyCode.BACKSLASH:
      case KeyCode.CLOSE_SQUARE_BRACKET:
        return true;

      default:
        return false;
    }
  }
};
/* harmony default export */ __webpack_exports__["a"] = (KeyCode);

/***/ }),
/* 5 */
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ })
/******/ ])["default"];
});
//# sourceMappingURL=rc-input-number.js.map