"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

var _interopRequireWildcard = require("@babel/runtime/helpers/interopRequireWildcard");

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.default = void 0;

var React = _interopRequireWildcard(require("react"));

var _TimeUnitColumn = _interopRequireDefault(require("./TimeUnitColumn"));

var _miscUtil = require("../../utils/miscUtil");

function generateUnits(start, end, step, disabledUnits) {
  var units = [];

  for (var i = start; i <= end; i += step) {
    units.push({
      label: (0, _miscUtil.leftPad)(i, 2),
      value: i,
      disabled: (disabledUnits || []).includes(i)
    });
  }

  return units;
}

function TimeBody(props) {
  var generateConfig = props.generateConfig,
      prefixCls = props.prefixCls,
      operationRef = props.operationRef,
      activeColumnIndex = props.activeColumnIndex,
      value = props.value,
      showHour = props.showHour,
      showMinute = props.showMinute,
      showSecond = props.showSecond,
      use12Hours = props.use12Hours,
      _props$hourStep = props.hourStep,
      hourStep = _props$hourStep === void 0 ? 1 : _props$hourStep,
      _props$minuteStep = props.minuteStep,
      minuteStep = _props$minuteStep === void 0 ? 1 : _props$minuteStep,
      _props$secondStep = props.secondStep,
      secondStep = _props$secondStep === void 0 ? 1 : _props$secondStep,
      disabledHours = props.disabledHours,
      disabledMinutes = props.disabledMinutes,
      disabledSeconds = props.disabledSeconds,
      hideDisabledOptions = props.hideDisabledOptions,
      onSelect = props.onSelect;
  var columns = [];
  var contentPrefixCls = "".concat(prefixCls, "-content");
  var columnPrefixCls = "".concat(prefixCls, "-time-panel");
  var isPM;
  var hour = value ? generateConfig.getHour(value) : -1;
  var minute = value ? generateConfig.getMinute(value) : -1;
  var second = value ? generateConfig.getSecond(value) : -1;

  var setTime = function setTime(isNewPM, newHour, newMinute, newSecond) {
    var newDate = value || generateConfig.getNow();
    var mergedHour = Math.max(0, newHour);
    var mergedMinute = Math.max(0, newMinute);
    var mergedSecond = Math.max(0, newSecond);
    newDate = generateConfig.setSecond(newDate, mergedSecond);
    newDate = generateConfig.setMinute(newDate, mergedMinute);
    newDate = generateConfig.setHour(newDate, !use12Hours || !isNewPM ? mergedHour : mergedHour + 12);
    return newDate;
  }; // ========================= Unit =========================


  var hours = generateUnits(0, use12Hours ? 11 : 23, hourStep, disabledHours && disabledHours()); // Should additional logic to handle 12 hours

  if (use12Hours && hour !== -1) {
    isPM = hour >= 12;
    hour %= 12;
    hours[0].label = '12';
  }

  var minutes = generateUnits(0, 59, minuteStep, disabledMinutes && disabledMinutes(hour));
  var seconds = generateUnits(0, 59, secondStep, disabledSeconds && disabledSeconds(hour, minute)); // ====================== Operations ======================

  operationRef.current = {
    onUpDown: function onUpDown(diff) {
      var column = columns[activeColumnIndex];

      if (column) {
        var valueIndex = column.units.findIndex(function (unit) {
          return unit.value === column.value;
        });
        var unitLen = column.units.length;

        for (var i = 1; i < unitLen; i += 1) {
          var nextUnit = column.units[(valueIndex + diff * i + unitLen) % unitLen];

          if (nextUnit.disabled !== true) {
            column.onSelect(nextUnit.value);
            break;
          }
        }
      }
    }
  }; // ======================== Render ========================

  function addColumnNode(condition, node, columnValue, units, onColumnSelect) {
    if (condition !== false) {
      columns.push({
        node: React.cloneElement(node, {
          prefixCls: columnPrefixCls,
          value: columnValue,
          active: activeColumnIndex === columns.length,
          onSelect: onColumnSelect,
          units: units,
          hideDisabledOptions: hideDisabledOptions
        }),
        onSelect: onColumnSelect,
        value: columnValue,
        units: units
      });
    }
  } // Hour


  addColumnNode(showHour, React.createElement(_TimeUnitColumn.default, {
    key: "hour"
  }), hour, hours, function (num) {
    onSelect(setTime(isPM, num, minute, second), 'mouse');
  }); // Minute

  addColumnNode(showMinute, React.createElement(_TimeUnitColumn.default, {
    key: "minute"
  }), minute, minutes, function (num) {
    onSelect(setTime(isPM, hour, num, second), 'mouse');
  }); // Second

  addColumnNode(showSecond, React.createElement(_TimeUnitColumn.default, {
    key: "second"
  }), second, seconds, function (num) {
    onSelect(setTime(isPM, hour, minute, num), 'mouse');
  }); // 12 Hours

  var PMIndex = -1;

  if (typeof isPM === 'boolean') {
    PMIndex = isPM ? 1 : 0;
  }

  addColumnNode(use12Hours === true, React.createElement(_TimeUnitColumn.default, {
    key: "12hours"
  }), PMIndex, [{
    label: 'AM',
    value: 0
  }, {
    label: 'PM',
    value: 1
  }], function (num) {
    onSelect(setTime(!!num, hour, minute, second), 'mouse');
  });
  return React.createElement("div", {
    className: contentPrefixCls
  }, columns.map(function (_ref) {
    var node = _ref.node;
    return node;
  }));
}

var _default = TimeBody;
exports.default = _default;