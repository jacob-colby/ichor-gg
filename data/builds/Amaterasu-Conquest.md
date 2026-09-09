---
type: smite-build
god: Amaterasu
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Daybreak Gavel
    pick_rate: 0.3
    win_rate: 0.69
    alternates:
    - name: Vital Amplifier
      pick_rate: 0.19
      win_rate: 0.75
    - name: Chronos' Pendant
      pick_rate: 0.16
      win_rate: 0.57
  - name: Shifter's Shield
    pick_rate: 0.12
    win_rate: 0.8
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.3
      win_rate: 0.85
    - name: Golden Blade
      pick_rate: 0.09
      win_rate: 0.75
  - name: Rod of Tahuti
    pick_rate: 0.14
    win_rate: 0.67
    alternates:
    - name: The World Stone
      pick_rate: 0.12
      win_rate: 0.6
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.8
  - name: Obsidian Shard
    pick_rate: 0.13
    win_rate: 0.8
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.1
      win_rate: 1.0
    - name: Kinetic Cuirass
      pick_rate: 0.1
      win_rate: 0.25
  - name: Shogun's Ofuda
    pick_rate: 0.14
    win_rate: 0.6
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 1.0
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 1.0
  - name: Shell of Rebuke
    pick_rate: 0.2
    win_rate: 0.8
    alternates:
    - name: Gem
      pick_rate: 0.08
      win_rate: 1.0
    - name: Dreamer's Idol
      pick_rate: 0.08
      win_rate: 1.0
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.28
    win_rate: 0.92
  - name: Sands Of Time
    pick_rate: 0.23
    win_rate: 0.5
  - name: Death's Embrace
    pick_rate: 0.19
    win_rate: 0.63
  source_url: https://smitebrain.com/gods/amaterasu/
  last_verified: '2026-09-09'
  god_win_rate: 0.7209302325581395
  god_matches_won: 31
  god_matches_played: 43
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-09'
  god_matches_analyzed: 921
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - Rod of Tahuti
  - Dreamer's Idol
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Rod of Tahuti
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Freya''s Tears, Shield Splitter, Genji''s
    Guard, Breastplate of Valor, Runeforged Hammer, Eye of the Storm, Erosion, Eye
    of Providence, Draconic Scale, Shield of the Phoenix, Hydra''s Lament, Stone of
    Binding, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Avenging Blade,
    Mantle Of Discord, Screeching Gargoyle, Midgardian Mail, Hide of the Nemean Lion,
    Spear of Desolation, Leviathan''s Hide, Void Shield, Stampede, Prophetic Cloak,
    Ancile, Heartseeker, Oni Hunter''s Garb, Rod of Asclepius, Soul Gem, Void Stone,
    Xibalban Effigy, Spectral Armor, Helm of Darkness, Spear of the Magus.'
  slot_scores:
    Berserker's Shield:
      total: 0.72
      efficiency: 0.6
      win: 1.0
      pick: 0.17
      fit: 0.36
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.75
      pick: 0.0
      fit: 0.38
    Shifter's Shield:
      total: 0.65
      efficiency: 0.55
      win: 0.8
      pick: 0.16
      fit: 0.57
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.67
      pick: 0.22
      fit: 0.1
    Dreamer's Idol:
      total: 0.66
      efficiency: 0.51
      win: 1.0
      pick: 0.25
      fit: 0.1
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Berserker's Shield
  - Shifter's Shield
  - Rod of Tahuti
  - Dreamer's Idol
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Shifter's Shield
  - Dreamer's Idol
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, Freya''s Tears,
    Rod of Asclepius, Runeforged Hammer, Soul Gem, Shield Splitter, Genji''s Guard,
    Breastplate of Valor, Eye of the Storm, Ethereal Staff, Erosion, Eye of Providence,
    The Reaper, Yogi''s Necklace, Draconic Scale, Hydra''s Lament, Phoenix Feather,
    Gluttonous Grimoire, Chandra''s Grace, Avenging Blade, Glorious Pridwen, Lifebinder,
    Stone of Binding, Midgardian Mail, Helm of Radiance, Hide of the Nemean Lion,
    Screeching Gargoyle, Sphere of Negation, Magi''s Cloak, Leviathan''s Hide, Spear
    of Desolation, Void Shield, Stampede, Ancile, Oni Hunter''s Garb.'
  slot_scores:
    Berserker's Shield:
      total: 0.73
      efficiency: 0.6
      win: 1.0
      pick: 0.17
      fit: 0.38
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.75
      pick: 0.0
      fit: 0.39
    Shield of the Phoenix:
      total: 0.64
      efficiency: 0.53
      win: 0.75
      pick: 0.0
      fit: 0.81
    Shifter's Shield:
      total: 0.64
      efficiency: 0.55
      win: 0.8
      pick: 0.16
      fit: 0.55
    Dreamer's Idol:
      total: 0.66
      efficiency: 0.51
      win: 1.0
      pick: 0.25
      fit: 0.11
    Amanita Charm:
      total: 0.69
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Berserker's Shield
  - Shifter's Shield
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Stone of Binding, Gluttonous Grimoire,
    Screeching Gargoyle, Avenging Blade, Freya''s Tears, Genji''s Guard, Spear of
    Desolation, Void Shield, Breastplate of Valor, Spear of the Magus, Heartseeker,
    Soul Gem, Shield Splitter, Void Stone, Runeforged Hammer, Titan''s Bane, The Crusher,
    Eye of the Storm, Erosion, Hydra''s Lament, The Reaper, Eye of Providence, Shield
    of the Phoenix, Draconic Scale, Helm of Radiance, Doom Orb, Magi''s Cloak, Pendulum
    Blade, Mantle Of Discord, Avatar''s Parashu, Midgardian Mail, Rod of Asclepius.'
  slot_scores:
    Berserker's Shield:
      total: 0.71
      efficiency: 0.6
      win: 1.0
      pick: 0.17
      fit: 0.27
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.72
      win: 0.75
      pick: 0.0
      fit: 0.54
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.67
      pick: 0.22
      fit: 0.34
    Obsidian Shard:
      total: 0.63
      efficiency: 0.54
      win: 0.8
      pick: 0.22
      fit: 0.44
    Dreamer's Idol:
      total: 0.69
      efficiency: 0.51
      win: 1.0
      pick: 0.25
      fit: 0.34
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Berserker's Shield
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Nimble Ring
  - Rod of Tahuti
  - Dreamer's Idol
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Nimble Ring, Golden Blade, Freya''s
    Tears, Genji''s Guard, Gluttonous Grimoire, Breastplate of Valor, Tyrfing, Shield
    Splitter, Soul Gem, Runeforged Hammer, Pharaoh''s Curse, Riptalon, Lernaean Bow,
    Silverbranch Bow, Erosion, Helm of Radiance, Hydra''s Lament, Shield of the Phoenix,
    Stone of Binding, Eye of Providence, Eye of the Storm, Toxic Blade, Draconic Scale,
    Magi''s Cloak, Screeching Gargoyle, Spear of Desolation, The Reaper, Spear of
    the Magus, Bragi''s Harp, Midgardian Mail, Mantle Of Discord, Tekko-Kagi, Rod
    of Asclepius, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.61
      efficiency: 0.52
      win: 0.75
      pick: 0.12
      fit: 0.53
    Berserker's Shield:
      total: 0.76
      efficiency: 0.68
      win: 1.0
      pick: 0.17
      fit: 0.43
    Nimble Ring:
      total: 0.61
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.3
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.67
      pick: 0.22
      fit: 0.07
    Dreamer's Idol:
      total: 0.65
      efficiency: 0.51
      win: 1.0
      pick: 0.25
      fit: 0.07
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Golden Blade
  - Berserker's Shield
  - Rod of Tahuti
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Rod of Tahuti
  - Dreamer's Idol
  flex_slots:
  - Genji's Guard
  - Rod of Tahuti
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Freya''s Tears,
    Genji''s Guard, Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Spear
    of Desolation, Hydra''s Lament, Screeching Gargoyle, Soul Gem, Shield Splitter,
    Prophetic Cloak, Erosion, Helm of Radiance, Runeforged Hammer, Gluttonous Grimoire,
    Eye of Providence, Gladiator''s Shield, Draconic Scale, Stone of Binding, Eye
    of the Storm, Arondight, Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of
    Erebus, Spear of the Magus, Mantle Of Discord, Glorious Pridwen, Midgardian Mail,
    Chandra''s Grace, Hide of the Nemean Lion, Leviathan''s Hide, Jade Scepter, Void
    Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.64
      efficiency: 0.66
      win: 0.75
      pick: 0.0
      fit: 0.48
    Berserker's Shield:
      total: 0.71
      efficiency: 0.6
      win: 1.0
      pick: 0.17
      fit: 0.29
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.75
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.65
      efficiency: 0.61
      win: 0.75
      pick: 0.0
      fit: 0.64
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.67
      pick: 0.22
      fit: 0.13
    Dreamer's Idol:
      total: 0.66
      efficiency: 0.51
      win: 1.0
      pick: 0.25
      fit: 0.13
  community_ordered:
  - Berserker's Shield
  - Rod of Tahuti
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  - Amanita Charm
  flex_slots:
  - Obsidian Shard
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm, Gluttonous
    Grimoire, Freya''s Tears, Spear of Desolation, Genji''s Guard, Breastplate of
    Valor, Soul Gem, Spear of the Magus, Helm of Radiance, Shield Splitter, Runeforged
    Hammer, Rod of Asclepius, Hydra''s Lament, Shield of the Phoenix, Eye of the Storm,
    Erosion, Jade Scepter, Doom Orb, Heartseeker, Eye of Providence, Wish-Granting
    Pearl, Stone of Binding, Draconic Scale, Ancient Signet, Death Metal, Helm of
    Darkness, Screeching Gargoyle, Magi''s Cloak, Avenging Blade, Ethereal Staff,
    Triton''s Conch, Mantle Of Discord.'
  slot_scores:
    Berserker's Shield:
      total: 0.71
      efficiency: 0.6
      win: 1.0
      pick: 0.17
      fit: 0.25
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.75
      pick: 0.0
      fit: 0.4
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.67
      pick: 0.22
      fit: 0.35
    Obsidian Shard:
      total: 0.63
      efficiency: 0.54
      win: 0.8
      pick: 0.22
      fit: 0.45
    Dreamer's Idol:
      total: 0.69
      efficiency: 0.51
      win: 1.0
      pick: 0.25
      fit: 0.35
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Berserker's Shield
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Gluttonous Grimoire, Freya''s Tears, Genji''s Guard, Breastplate of Valor, Spear
    of Desolation, Shield Splitter, Spear of the Magus, Soul Gem, Runeforged Hammer,
    Helm of Radiance, Eye of the Storm, Hydra''s Lament, Rod of Asclepius, Heartseeker,
    Erosion, Eye of Providence, Shield of the Phoenix, Stone of Binding, Draconic
    Scale, Doom Orb, Jade Scepter, Death Metal, Wish-Granting Pearl, Avenging Blade,
    Magi''s Cloak, Helm of Darkness, Titan''s Bane, Screeching Gargoyle, Ancient Signet,
    The Crusher, Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.71
      efficiency: 0.6
      win: 1.0
      pick: 0.17
      fit: 0.26
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.75
      pick: 0.0
      fit: 0.41
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.67
      pick: 0.22
      fit: 0.32
    Obsidian Shard:
      total: 0.63
      efficiency: 0.54
      win: 0.8
      pick: 0.22
      fit: 0.42
    Dreamer's Idol:
      total: 0.69
      efficiency: 0.51
      win: 1.0
      pick: 0.25
      fit: 0.32
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Berserker's Shield
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Jotunn''s Revenge, Freya''s Tears, Shield
    Splitter, Genji''s Guard, Breastplate of Valor, Runeforged Hammer, Eye of the
    Storm, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Hydra''s
    Lament, Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire,
    Avenging Blade, Mantle Of Discord, Screeching Gargoyle, Midgardian Mail, Hide
    of the Nemean Lion, Spear of Desolation, Leviathan''s Hide, Void Shield, Stampede,
    Prophetic Cloak, Ancile, Heartseeker, Oni Hunter''s Garb, Rod of Asclepius, Soul
    Gem, Void Stone, Xibalban Effigy, Spectral Armor, Helm of Darkness, Spear of the
    Magus.'
  slot_scores:
    Genji's Guard:
      total: 0.62
      efficiency: 0.66
      win: 0.75
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.75
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.42
      efficiency: 0.56
      win: 0.25
      pick: 0.17
      fit: 0.67
    Shield Splitter:
      total: 0.62
      efficiency: 0.55
      win: 0.75
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.75
      pick: 0.0
      fit: 0.53
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Kinetic Cuirass
  starter: *id001
---
