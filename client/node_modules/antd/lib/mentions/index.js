"use strict";

function _typeof(obj) { "@babel/helpers - typeof"; if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = exports.Option = void 0;

var React = _interopRequireWildcard(require("react"));

var _classnames = _interopRequireDefault(require("classnames"));

var _rcMentions = _interopRequireDefault(require("rc-mentions"));

var _spin = _interopRequireDefault(require("../spin"));

var _configProvider = require("../config-provider");

var _ref2 = require("../_util/ref");

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

function _getRequireWildcardCache() { if (typeof WeakMap !== "function") return null; var cache = new WeakMap(); _getRequireWildcardCache = function _getRequireWildcardCache() { return cache; }; return cache; }

function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } if (obj === null || _typeof(obj) !== "object" && typeof obj !== "function") { return { "default": obj }; } var cache = _getRequireWildcardCache(); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj["default"] = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

function _extends() { _extends = Object.assign || function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; }; return _extends.apply(this, arguments); }

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

function _slicedToArray(arr, i) { return _arrayWithHoles(arr) || _iterableToArrayLimit(arr, i) || _unsupportedIterableToArray(arr, i) || _nonIterableRest(); }

function _nonIterableRest() { throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); }

function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }

function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }

function _iterableToArrayLimit(arr, i) { if (typeof Symbol === "undefined" || !(Symbol.iterator in Object(arr))) return; var _arr = []; var _n = true; var _d = false; var _e = undefined; try { for (var _i = arr[Symbol.iterator](), _s; !(_n = (_s = _i.next()).done); _n = true) { _arr.push(_s.value); if (i && _arr.length === i) break; } } catch (err) { _d = true; _e = err; } finally { try { if (!_n && _i["return"] != null) _i["return"](); } finally { if (_d) throw _e; } } return _arr; }

function _arrayWithHoles(arr) { if (Array.isArray(arr)) return arr; }

var __rest = void 0 && (void 0).__rest || function (s, e) {
  var t = {};

  for (var p in s) {
    if (Object.prototype.hasOwnProperty.call(s, p) && e.indexOf(p) < 0) t[p] = s[p];
  }

  if (s != null && typeof Object.getOwnPropertySymbols === "function") for (var i = 0, p = Object.getOwnPropertySymbols(s); i < p.length; i++) {
    if (e.indexOf(p[i]) < 0 && Object.prototype.propertyIsEnumerable.call(s, p[i])) t[p[i]] = s[p[i]];
  }
  return t;
};

var Option = _rcMentions["default"].Option;
exports.Option = Option;

function loadingFilterOption() {
  return true;
}

var InternalMentions = function InternalMentions(_a, ref) {
  var _classNames;

  var customizePrefixCls = _a.prefixCls,
      className = _a.className,
      disabled = _a.disabled,
      loading = _a.loading,
      filterOption = _a.filterOption,
      children = _a.children,
      notFoundContent = _a.notFoundContent,
      restProps = __rest(_a, ["prefixCls", "className", "disabled", "loading", "filterOption", "children", "notFoundContent"]);

  var _React$useState = React.useState(false),
      _React$useState2 = _slicedToArray(_React$useState, 2),
      focused = _React$useState2[0],
      setFocused = _React$useState2[1];

  var innerRef = React.useRef();
  var mergedRef = (0, _ref2.composeRef)(ref, innerRef);

  var _React$useContext = React.useContext(_configProvider.ConfigContext),
      getPrefixCls = _React$useContext.getPrefixCls,
      renderEmpty = _React$useContext.renderEmpty,
      direction = _React$useContext.direction;

  var onFocus = function onFocus() {
    if (restProps.onFocus) {
      restProps.onFocus.apply(restProps, arguments);
    }

    setFocused(true);
  };

  var onBlur = function onBlur() {
    if (restProps.onBlur) {
      restProps.onBlur.apply(restProps, arguments);
    }

    setFocused(false);
  };

  var getNotFoundContent = function getNotFoundContent() {
    if (notFoundContent !== undefined) {
      return notFoundContent;
    }

    return renderEmpty('Select');
  };

  var getOptions = function getOptions() {
    if (loading) {
      return /*#__PURE__*/React.createElement(Option, {
        value: "ANTD_SEARCHING",
        disabled: true
      }, /*#__PURE__*/React.createElement(_spin["default"], {
        size: "small"
      }));
    }

    return children;
  };

  var getFilterOption = function getFilterOption() {
    if (loading) {
      return loadingFilterOption;
    }

    return filterOption;
  };

  var prefixCls = getPrefixCls('mentions', customizePrefixCls);
  var mergedClassName = (0, _classnames["default"])(className, (_classNames = {}, _defineProperty(_classNames, "".concat(prefixCls, "-disabled"), disabled), _defineProperty(_classNames, "".concat(prefixCls, "-focused"), focused), _defineProperty(_classNames, "".concat(prefixCls, "-rtl"), direction === 'rtl'), _classNames));
  return /*#__PURE__*/React.createElement(_rcMentions["default"], _extends({
    prefixCls: prefixCls,
    notFoundContent: getNotFoundContent(),
    className: mergedClassName,
    disabled: disabled,
    direction: direction
  }, restProps, {
    filterOption: getFilterOption(),
    onFocus: onFocus,
    onBlur: onBlur,
    ref: mergedRef
  }), getOptions());
};

var Mentions = /*#__PURE__*/React.forwardRef(InternalMentions);
Mentions.displayName = 'Mentions';
Mentions.Option = Option;

Mentions.getMentions = function () {
  var value = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : '';
  var config = arguments.length > 1 ? arguments[1] : undefined;

  var _ref = config || {},
      _ref$prefix = _ref.prefix,
      prefix = _ref$prefix === void 0 ? '@' : _ref$prefix,
      _ref$split = _ref.split,
      split = _ref$split === void 0 ? ' ' : _ref$split;

  var prefixList = Array.isArray(prefix) ? prefix : [prefix];
  return value.split(split).map(function () {
    var str = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : '';
    var hitPrefix = null;
    prefixList.some(function (prefixStr) {
      var startStr = str.slice(0, prefixStr.length);

      if (startStr === prefixStr) {
        hitPrefix = prefixStr;
        return true;
      }

      return false;
    });

    if (hitPrefix !== null) {
      return {
        prefix: hitPrefix,
        value: str.slice(hitPrefix.length)
      };
    }

    return null;
  }).filter(function (entity) {
    return !!entity && !!entity.value;
  });
};

var _default = Mentions;
exports["default"] = _default;