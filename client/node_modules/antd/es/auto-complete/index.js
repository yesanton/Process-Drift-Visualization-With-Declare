function _extends() { _extends = Object.assign || function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; }; return _extends.apply(this, arguments); }

function _typeof(obj) { "@babel/helpers - typeof"; if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

function _slicedToArray(arr, i) { return _arrayWithHoles(arr) || _iterableToArrayLimit(arr, i) || _unsupportedIterableToArray(arr, i) || _nonIterableRest(); }

function _nonIterableRest() { throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); }

function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }

function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }

function _iterableToArrayLimit(arr, i) { if (typeof Symbol === "undefined" || !(Symbol.iterator in Object(arr))) return; var _arr = []; var _n = true; var _d = false; var _e = undefined; try { for (var _i = arr[Symbol.iterator](), _s; !(_n = (_s = _i.next()).done); _n = true) { _arr.push(_s.value); if (i && _arr.length === i) break; } } catch (err) { _d = true; _e = err; } finally { try { if (!_n && _i["return"] != null) _i["return"](); } finally { if (_d) throw _e; } } return _arr; }

function _arrayWithHoles(arr) { if (Array.isArray(arr)) return arr; }

/**
 * TODO: 4.0
 * - remove `dataSource`
 * - `size` not work with customizeInput
 * - customizeInput not feedback `ENTER` key since accessibility enhancement
 */
import * as React from 'react';
import toArray from "rc-util/es/Children/toArray";
import classNames from 'classnames';
import omit from 'omit.js';
import Select from '../select';
import { ConfigConsumer } from '../config-provider';
import devWarning from '../_util/devWarning';
import { isValidElement } from '../_util/reactNode';
var Option = Select.Option;
var InternalSelect = Select;

function isSelectOptionOrSelectOptGroup(child) {
  return child && child.type && (child.type.isSelectOption || child.type.isSelectOptGroup);
}

var AutoComplete = function AutoComplete(props, ref) {
  var customizePrefixCls = props.prefixCls,
      className = props.className,
      children = props.children,
      dataSource = props.dataSource;
  var childNodes = toArray(children);
  var selectRef = React.useRef();
  React.useImperativeHandle(ref, function () {
    return selectRef.current;
  }); // ============================= Input =============================

  var customizeInput;

  if (childNodes.length === 1 && isValidElement(childNodes[0]) && !isSelectOptionOrSelectOptGroup(childNodes[0])) {
    var _childNodes = _slicedToArray(childNodes, 1);

    customizeInput = _childNodes[0];
  }

  var getInputElement = function getInputElement() {
    return customizeInput;
  }; // ============================ Options ============================


  var optionChildren; // [Legacy] convert `children` or `dataSource` into option children

  if (childNodes.length && isSelectOptionOrSelectOptGroup(childNodes[0])) {
    optionChildren = children;
  } else {
    optionChildren = dataSource ? dataSource.map(function (item) {
      if (isValidElement(item)) {
        return item;
      }

      switch (_typeof(item)) {
        case 'string':
          return /*#__PURE__*/React.createElement(Option, {
            key: item,
            value: item
          }, item);

        case 'object':
          {
            var optionValue = item.value;
            return /*#__PURE__*/React.createElement(Option, {
              key: optionValue,
              value: optionValue
            }, item.text);
          }

        default:
          throw new Error('AutoComplete[dataSource] only supports type `string[] | Object[]`.');
      }
    }) : [];
  } // ============================ Warning ============================


  React.useEffect(function () {
    devWarning(!('dataSource' in props), 'AutoComplete', '`dataSource` is deprecated, please use `options` instead.');
    devWarning(!customizeInput || !('size' in props), 'AutoComplete', 'You need to control style self instead of setting `size` when using customize input.');
  }, []);
  return /*#__PURE__*/React.createElement(ConfigConsumer, null, function (_ref) {
    var getPrefixCls = _ref.getPrefixCls;
    var prefixCls = getPrefixCls('select', customizePrefixCls);
    return /*#__PURE__*/React.createElement(InternalSelect, _extends({
      ref: selectRef
    }, omit(props, ['dataSource']), {
      prefixCls: prefixCls,
      className: classNames(className, "".concat(prefixCls, "-auto-complete")),
      mode: Select.SECRET_COMBOBOX_MODE_DO_NOT_USE,
      getInputElement: getInputElement
    }), optionChildren);
  });
};

var RefAutoComplete = /*#__PURE__*/React.forwardRef(AutoComplete);
RefAutoComplete.Option = Option;
export default RefAutoComplete;