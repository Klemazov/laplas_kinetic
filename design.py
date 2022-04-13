<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1227</width>
    <height>876</height>
   </rect>
  </property>
  <property name="sizePolicy">
   <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
    <horstretch>0</horstretch>
    <verstretch>0</verstretch>
   </sizepolicy>
  </property>
  <property name="windowTitle">
   <string>Activation energy calculation</string>
  </property>
  <property name="accessibleName">
   <string notr="true"/>
  </property>
  <property name="styleSheet">
   <string notr="true"/>
  </property>
  <property name="toolButtonStyle">
   <enum>Qt::ToolButtonIconOnly</enum>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="ActivationEnergyButton">
    <property name="geometry">
     <rect>
      <x>480</x>
      <y>260</y>
      <width>251</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>17</pointsize>
     </font>
    </property>
    <property name="text">
     <string>calculate Ea</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>790</x>
      <y>-10</y>
      <width>211</width>
      <height>121</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>24</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Ea, kJ/mol</string>
    </property>
   </widget>
   <widget class="QLCDNumber" name="lcdEnergy">
    <property name="geometry">
     <rect>
      <x>980</x>
      <y>10</y>
      <width>221</width>
      <height>91</height>
     </rect>
    </property>
    <property name="autoFillBackground">
     <bool>false</bool>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 10pt &quot;MS Shell Dlg 2&quot;;</string>
    </property>
    <property name="smallDecimalPoint">
     <bool>false</bool>
    </property>
    <property name="segmentStyle">
     <enum>QLCDNumber::Flat</enum>
    </property>
   </widget>
   <widget class="QWidget" name="layoutWidget">
    <property name="geometry">
     <rect>
      <x>480</x>
      <y>120</y>
      <width>251</width>
      <height>141</height>
     </rect>
    </property>
    <layout class="QGridLayout" name="gridLayout">
     <item row="1" column="0">
      <widget class="QLineEdit" name="HeatingRate2">
       <property name="font">
        <font>
         <pointsize>14</pointsize>
        </font>
       </property>
      </widget>
     </item>
     <item row="0" column="0">
      <widget class="QLineEdit" name="HeatingRate1">
       <property name="font">
        <font>
         <pointsize>14</pointsize>
        </font>
       </property>
      </widget>
     </item>
     <item row="0" column="1">
      <widget class="QLineEdit" name="Temperature1">
       <property name="font">
        <font>
         <pointsize>14</pointsize>
        </font>
       </property>
      </widget>
     </item>
     <item row="1" column="1">
      <widget class="QLineEdit" name="Temperature2">
       <property name="font">
        <font>
         <pointsize>14</pointsize>
        </font>
       </property>
      </widget>
     </item>
     <item row="2" column="1">
      <widget class="QLineEdit" name="Temperature3">
       <property name="font">
        <font>
         <pointsize>14</pointsize>
        </font>
       </property>
      </widget>
     </item>
     <item row="2" column="0">
      <widget class="QLineEdit" name="HeatingRate3">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Expanding" vsizetype="Minimum">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="font">
        <font>
         <pointsize>14</pointsize>
        </font>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QLabel" name="StderrLabel">
    <property name="geometry">
     <rect>
      <x>800</x>
      <y>110</y>
      <width>201</width>
      <height>91</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>24</pointsize>
     </font>
    </property>
    <property name="text">
     <string>STD error</string>
    </property>
   </widget>
   <widget class="QLabel" name="R2Label">
    <property name="geometry">
     <rect>
      <x>870</x>
      <y>220</y>
      <width>111</width>
      <height>61</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>24</pointsize>
     </font>
    </property>
    <property name="text">
     <string>R^2</string>
    </property>
   </widget>
   <widget class="QLCDNumber" name="lcdNumberSTD">
    <property name="geometry">
     <rect>
      <x>980</x>
      <y>110</y>
      <width>221</width>
      <height>91</height>
     </rect>
    </property>
   </widget>
   <widget class="QLCDNumber" name="lcdNumberR2">
    <property name="geometry">
     <rect>
      <x>980</x>
      <y>210</y>
      <width>221</width>
      <height>91</height>
     </rect>
    </property>
   </widget>
   <widget class="MplWidget" name="MplWidget" native="true">
    <property name="geometry">
     <rect>
      <x>580</x>
      <y>330</y>
      <width>621</width>
      <height>481</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">border-color: rgb(170, 170, 255);</string>
    </property>
   </widget>
   <widget class="MplWidget" name="widgetDSC" native="true">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>330</y>
      <width>531</width>
      <height>481</height>
     </rect>
    </property>
   </widget>
   <widget class="QComboBox" name="comboBoxSelectDsc">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>130</y>
      <width>201</width>
      <height>51</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="pushDscButton">
    <property name="geometry">
     <rect>
      <x>230</x>
      <y>130</y>
      <width>201</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true"/>
    </property>
    <property name="text">
     <string>plot dsc</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineTemperatureMin">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>250</y>
      <width>113</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineTemperatureMax">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>280</y>
      <width>113</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButtonFindTemperature">
    <property name="geometry">
     <rect>
      <x>230</x>
      <y>190</y>
      <width>201</width>
      <height>71</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>9</pointsize>
     </font>
    </property>
    <property name="text">
     <string>maximum temperature</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>245</y>
      <width>55</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>14</pointsize>
     </font>
    </property>
    <property name="text">
     <string>from</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>275</y>
      <width>55</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>14</pointsize>
     </font>
    </property>
    <property name="text">
     <string>to</string>
    </property>
   </widget>
   <widget class="QLCDNumber" name="lcdNumberExtremumTemperature">
    <property name="geometry">
     <rect>
      <x>230</x>
      <y>260</y>
      <width>201</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label_6">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>40</y>
      <width>271</width>
      <height>61</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>MS Shell Dlg 2</family>
      <pointsize>20</pointsize>
      <underline>false</underline>
     </font>
    </property>
    <property name="text">
     <string>Check DSC curves</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_7">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>210</y>
      <width>201</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>14</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Temperature range</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>480</x>
      <y>90</y>
      <width>141</width>
      <height>28</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="text">
     <string>heating rate K/min</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>620</x>
      <y>90</y>
      <width>121</width>
      <height>28</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Temperature C</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_8">
    <property name="geometry">
     <rect>
      <x>500</x>
      <y>40</y>
      <width>55</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="Line" name="line">
    <property name="geometry">
     <rect>
      <x>443</x>
      <y>0</y>
      <width>20</width>
      <height>321</height>
     </rect>
    </property>
    <property name="orientation">
     <enum>Qt::Vertical</enum>
    </property>
   </widget>
   <widget class="Line" name="line_2">
    <property name="geometry">
     <rect>
      <x>550</x>
      <y>330</y>
      <width>20</width>
      <height>511</height>
     </rect>
    </property>
    <property name="orientation">
     <enum>Qt::Vertical</enum>
    </property>
   </widget>
   <widget class="QLabel" name="label_9">
    <property name="geometry">
     <rect>
      <x>500</x>
      <y>30</y>
      <width>221</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>14</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Input data from DSC </string>
    </property>
   </widget>
   <widget class="Line" name="line_3">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>310</y>
      <width>1221</width>
      <height>16</height>
     </rect>
    </property>
    <property name="orientation">
     <enum>Qt::Horizontal</enum>
    </property>
   </widget>
   <widget class="Line" name="line_4">
    <property name="geometry">
     <rect>
      <x>760</x>
      <y>0</y>
      <width>20</width>
      <height>321</height>
     </rect>
    </property>
    <property name="orientation">
     <enum>Qt::Vertical</enum>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1227</width>
     <height>37</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>14</pointsize>
    </font>
   </property>
   <widget class="QMenu" name="menuopen">
    <property name="font">
     <font>
      <pointsize>14</pointsize>
     </font>
    </property>
    <property name="title">
     <string>File</string>
    </property>
   </widget>
   <addaction name="menuopen"/>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
  <action name="actionopen">
   <property name="text">
    <string>open</string>
   </property>
  </action>
 </widget>
 <customwidgets>
  <customwidget>
   <class>MplWidget</class>
   <extends>QWidget</extends>
   <header>mplwidget.h</header>
   <container>1</container>
  </customwidget>
 </customwidgets>
 <resources/>
 <connections/>
</ui>
