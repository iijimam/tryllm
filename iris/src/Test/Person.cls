Class Test.Person Extends %Persistent
{

Property PID As %Integer;

Property Name As %String;

Property DOB As %Date;

Property Gender As %String;

Property Age As %Integer [ Calculated, SqlComputeCode = { set {*}=($H-{DOB})\365.25 }, SqlComputed ];

/// LOAD DATAのファイル指定はビルド時のパス指定。単独実行時は実行時のパスに変えること！
ClassMethod load()
{
    &sql(
    LOAD DATA FROM FILE '/opt/src/persons.csv'
    INTO Test.Person (PID,Name,DOB,Gender)
    USING {"from":{"file":{"charset":"UTF-8","header":true}}}
    )
    if SQLCODE<0 {
        write %msg,!
    }
}

Storage Default
{
<Data name="PersonDefaultData">
<Value name="1">
<Value>%%CLASSNAME</Value>
</Value>
<Value name="2">
<Value>PID</Value>
</Value>
<Value name="3">
<Value>Name</Value>
</Value>
<Value name="4">
<Value>DOB</Value>
</Value>
<Value name="5">
<Value>Gender</Value>
</Value>
</Data>
<DataLocation>^Test.PersonD</DataLocation>
<DefaultData>PersonDefaultData</DefaultData>
<IdLocation>^Test.PersonD</IdLocation>
<IndexLocation>^Test.PersonI</IndexLocation>
<StreamLocation>^Test.PersonS</StreamLocation>
<Type>%Storage.Persistent</Type>
}

}
