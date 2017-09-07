<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1339</width>
    <height>734</height>
   </rect>
  </property>
  <property name="maximumSize">
   <size>
    <width>3840</width>
    <height>2160</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QGridLayout" name="gridLayout">
    <item row="2" column="2">
     <widget class="QGroupBox" name="plotCtrl">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Preferred" vsizetype="Expanding">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="minimumSize">
       <size>
        <width>0</width>
        <height>150</height>
       </size>
      </property>
      <property name="title">
       <string>Plot Control</string>
      </property>
      <property name="alignment">
       <set>Qt::AlignHCenter|Qt::AlignTop</set>
      </property>
      <property name="flat">
       <bool>true</bool>
      </property>
      <layout class="QVBoxLayout" name="verticalLayout">
       <property name="margin">
        <number>0</number>
       </property>
       <item>
        <widget class="QRadioButton" name="motor_temp">
         <property name="text">
          <string>Motor Temperature</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QRadioButton" name="oil_temp">
         <property name="text">
          <string>Oil Temperature</string>
         </property>
        </widget>
       </item>
      </layout>
     </widget>
    </item>
    <item row="3" column="2">
     <widget class="PlotWidget" name="plot">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Expanding" vsizetype="Minimum">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="minimumSize">
       <size>
        <width>0</width>
        <height>500</height>
       </size>
      </property>
     </widget>
    </item>
    <item row="0" column="0" rowspan="4">
     <widget class="QTabWidget" name="tabWidget">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Expanding">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="minimumSize">
       <size>
        <width>450</width>
        <height>0</height>
       </size>
      </property>
      <property name="currentIndex">
       <number>0</number>
      </property>
      <widget class="QWidget" name="generalTAb">
       <attribute name="title">
        <string>Tab 1</string>
       </attribute>
       <layout class="QGridLayout" name="gridLayout_4">
        <item row="0" column="0">
         <widget class="QLabel" name="temperture">
          <property name="text">
           <string>Temperature</string>
          </property>
         </widget>
        </item>
        <item row="0" column="1">
         <widget class="QCheckBox" name="cB_tempreture">
          <property name="text">
           <string>Invert</string>
          </property>
         </widget>
        </item>
        <item row="1" column="1">
         <widget class="QLCDNumber" name="lcd_temperature"/>
        </item>
        <item row="2" column="0">
         <widget class="QLabel" name="oil_temp_2">
          <property name="text">
           <string>Oil Temperature</string>
          </property>
         </widget>
        </item>
        <item row="2" column="1">
         <widget class="QCheckBox" name="cB_oil_temp">
          <property name="text">
           <string>Invert</string>
          </property>
         </widget>
        </item>
        <item row="3" column="1">
         <widget class="QLCDNumber" name="lcd_oil_temp"/>
        </item>
        <item row="4" column="0">
         <widget class="QLabel" name="Fuel">
          <property name="text">
           <string>Fuel Level</string>
          </property>
         </widget>
        </item>
        <item row="4" column="1">
         <widget class="QCheckBox" name="cB_fuel">
          <property name="text">
           <string>Invert</string>
          </property>
         </widget>
        </item>
        <item row="5" column="1">
         <widget class="QLCDNumber" name="lcd_fuel"/>
        </item>
        <item row="6" column="0">
         <widget class="QLabel" name="water">
          <property name="text">
           <string>Water Level</string>
          </property>
         </widget>
        </item>
        <item row="6" column="1">
         <widget class="QCheckBox" name="cB_water">
          <property name="text">
           <string>Invert</string>
          </property>
         </widget>
        </item>
        <item row="7" column="1">
         <widget class="QLCDNumber" name="lcd_water"/>
        </item>
        <item row="8" column="0">
         <widget class="QLabel" name="In">
          <property name="text">
           <string>Cut In</string>
          </property>
         </widget>
        </item>
        <item row="9" column="1">
         <widget class="QLCDNumber" name="lcd_In"/>
        </item>
        <item row="10" column="0">
         <widget class="QLabel" name="Out">
          <property name="text">
           <string>Cut Out</string>
          </property>
         </widget>
        </item>
        <item row="10" column="1">
         <widget class="QCheckBox" name="cB_Out">
          <property name="text">
           <string>Invert</string>
          </property>
         </widget>
        </item>
        <item row="11" column="1">
         <widget class="QLCDNumber" name="lcd_Out"/>
        </item>
        <item row="8" column="1">
         <widget class="QCheckBox" name="cB_In">
          <property name="text">
           <string>Invert</string>
          </property>
         </widget>
        </item>
       </layout>
      </widget>
      <widget class="QWidget" name="serialTab">
       <property name="locale">
        <locale language="English" country="UnitedKingdom"/>
       </property>
       <attribute name="title">
        <string>Tab 2</string>
       </attribute>
       <layout class="QGridLayout" name="gridLayout_2">
        <item row="0" column="0">
         <widget class="QLabel" name="label">
          <property name="text">
           <string>Port</string>
          </property>
         </widget>
        </item>
        <item row="1" column="0">
         <widget class="QComboBox" name="comPort">
          <property name="currentText" stdset="0">
           <string/>
          </property>
         </widget>
        </item>
        <item row="2" column="0">
         <widget class="QLabel" name="label_2">
          <property name="text">
           <string>Buadrate</string>
          </property>
         </widget>
        </item>
        <item row="3" column="0">
         <widget class="QComboBox" name="buadrate">
          <property name="currentText" stdset="0">
           <string/>
          </property>
         </widget>
        </item>
        <item row="4" column="0">
         <widget class="QLabel" name="label_3">
          <property name="text">
           <string>Serial Input</string>
          </property>
         </widget>
        </item>
        <item row="5" column="0">
         <widget class="QTextBrowser" name="serialBrowser"/>
        </item>
       </layout>
      </widget>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1339</width>
     <height>25</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <customwidgets>
  <customwidget>
   <class>PlotWidget</class>
   <extends>QGraphicsView</extends>
   <header>pyqtgraph</header>
  </customwidget>
 </customwidgets>
 <resources/>
 <connections/>
</ui>
