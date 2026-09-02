---
type: smite-build
god: Chaac
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fulmination
  aspect_pick_rate: 0.2
  aspect_win_rate: 0.5
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.22
    win_rate: 0.42
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.14
      win_rate: 0.53
    - name: Book of Thoth
      pick_rate: 0.13
      win_rate: 0.36
  - name: Breastplate of Valor
    pick_rate: 0.13
    win_rate: 0.43
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.19
      win_rate: 0.52
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.13
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.5
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.45
    - name: Gladiator's Shield
      pick_rate: 0.05
      win_rate: 0.6
  - name: The World Stone
    pick_rate: 0.07
    win_rate: 0.43
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.42
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.43
  - name: Rod of Tahuti
    pick_rate: 0.05
    win_rate: 0.6
    alternates:
    - name: The World Stone
      pick_rate: 0.05
      win_rate: 0.2
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.0
  - name: Shield
    pick_rate: 0.05
    win_rate: 0.0
    alternates:
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.33
    - name: Sage's Ring
      pick_rate: 0.05
      win_rate: 0.33
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.38
    win_rate: 0.61
  - name: Bluestone Pendant
    pick_rate: 0.18
    win_rate: 0.45
  - name: Pendulum of the Ages
    pick_rate: 0.17
    win_rate: 0.28
  source_url: https://smitebrain.com/gods/chaac/
  last_verified: '2026-09-02'
  god_win_rate: 0.48623853211009177
  god_matches_won: 53
  god_matches_played: 109
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-09-01'
  god_matches_analyzed: 8200
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Daybreak Gavel, Kinetic
    Cuirass, Freya''s Tears, Gluttonous Grimoire, Shield Splitter, Spear of Desolation,
    Runeforged Hammer, Spear of the Magus, Helm of Radiance, Soul Gem, Berserker''s
    Shield, Obsidian Shard, Eye of the Storm, Erosion, Eye of Providence, Hydra''s
    Lament, Draconic Scale, Heartseeker, Shield of the Phoenix, Stone of Binding,
    Rod of Asclepius, The World Stone, Magi''s Cloak, Avenging Blade, Jade Scepter,
    Doom Orb, Screeching Gargoyle, Wish-Granting Pearl, Mantle Of Discord, Helm of
    Darkness, Midgardian Mail, Titan''s Bane, Death Metal, Chronos'' Pendant, The
    Crusher, Hide of the Nemean Lion.'
  slot_scores:
    Book of Thoth:
      total: 0.37
      efficiency: 0.51
      win: 0.36
      pick: 0.13
      fit: 0.15
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.26
      fit: 0.24
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.42
      pick: 0.0
      fit: 0.4
    Transcendence:
      total: 0.4
      efficiency: 0.53
      win: 0.42
      pick: 0.0
      fit: 0.17
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.6
      pick: 0.11
      fit: 0.3
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.45
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Gladiator's Shield
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Jotunn''s Revenge, Amanita Charm, Daybreak Gavel, Freya''s Tears, Gluttonous
    Grimoire, Kinetic Cuirass, Spear of Desolation, Shield Splitter, Spear of the
    Magus, Hydra''s Lament, Runeforged Hammer, Helm of Radiance, Soul Gem, Obsidian
    Shard, Heartseeker, Berserker''s Shield, The World Stone, Eye of the Storm, Rod
    of Asclepius, Wish-Granting Pearl, Doom Orb, Ancient Signet, Shield of the Phoenix,
    Erosion, Death Metal, Chronos'' Pendant, Jade Scepter, Stone of Binding, Eye of
    Providence, Avenging Blade, Draconic Scale, Screeching Gargoyle, Magi''s Cloak,
    Titan''s Bane, Helm of Darkness, Triton''s Conch, The Crusher, Oni Hunter''s Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.26
      fit: 0.29
    Breastplate of Valor:
      total: 0.47
      efficiency: 0.65
      win: 0.43
      pick: 0.18
      fit: 0.29
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.42
      pick: 0.0
      fit: 0.45
    Gladiator's Shield:
      total: 0.48
      efficiency: 0.39
      win: 0.6
      pick: 0.08
      fit: 0.42
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.6
      pick: 0.11
      fit: 0.36
    Amanita Charm:
      total: 0.47
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Gladiator's Shield
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Daybreak Gavel, Freya''s
    Tears, Gluttonous Grimoire, Spear of Desolation, Kinetic Cuirass, Soul Gem, Spear
    of the Magus, Obsidian Shard, Shield Splitter, Runeforged Hammer, Helm of Radiance,
    Berserker''s Shield, Hydra''s Lament, Heartseeker, Shield of the Phoenix, The
    World Stone, Eye of the Storm, Erosion, Doom Orb, Rod of Asclepius, Eye of Providence,
    Screeching Gargoyle, Stone of Binding, Chronos'' Pendant, Draconic Scale, Titan''s
    Bane, The Crusher, Dreamer''s Idol, Magi''s Cloak, Jade Scepter, The Reaper, Wish-Granting
    Pearl, Avenging Blade, Mantle Of Discord, Midgardian Mail, Ancient Signet.'
  slot_scores:
    Book of Thoth:
      total: 0.37
      efficiency: 0.51
      win: 0.36
      pick: 0.13
      fit: 0.14
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.26
      fit: 0.27
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.42
      pick: 0.0
      fit: 0.48
    Transcendence:
      total: 0.4
      efficiency: 0.53
      win: 0.42
      pick: 0.0
      fit: 0.14
    Gladiator's Shield:
      total: 0.48
      efficiency: 0.39
      win: 0.6
      pick: 0.08
      fit: 0.48
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.6
      pick: 0.11
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Soul Gem, Rod of Asclepius,
    Shield of the Phoenix, Daybreak Gavel, Gluttonous Grimoire, Kinetic Cuirass, Ethereal
    Staff, The Reaper, Freya''s Tears, Runeforged Hammer, Spear of Desolation, Spear
    of the Magus, Shield Splitter, Berserker''s Shield, Lifebinder, Obsidian Shard,
    Helm of Radiance, Eye of the Storm, Yogi''s Necklace, Sphere of Negation, Hydra''s
    Lament, Erosion, Heartseeker, Phoenix Feather, Eye of Providence, Chandra''s Grace,
    Draconic Scale, Avenging Blade, Blood-Bound Book, Jade Scepter, Wish-Granting
    Pearl, Stone of Binding, Doom Orb, Glorious Pridwen, Midgardian Mail, Titan''s
    Bane.'
  slot_scores:
    Book of Thoth:
      total: 0.37
      efficiency: 0.51
      win: 0.36
      pick: 0.13
      fit: 0.16
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.26
      fit: 0.22
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.42
      pick: 0.0
      fit: 0.42
    Transcendence:
      total: 0.4
      efficiency: 0.53
      win: 0.42
      pick: 0.0
      fit: 0.17
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.6
      pick: 0.11
      fit: 0.31
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire,
    Stone of Binding, Daybreak Gavel, Spear of Desolation, Spear of the Magus, Avenging
    Blade, Kinetic Cuirass, Screeching Gargoyle, Soul Gem, Freya''s Tears, Obsidian
    Shard, Void Shield, Heartseeker, Void Stone, Shield Splitter, Runeforged Hammer,
    The World Stone, Helm of Radiance, Berserker''s Shield, Doom Orb, Titan''s Bane,
    The Crusher, Eye of the Storm, Hydra''s Lament, Dreamer''s Idol, Erosion, The
    Reaper, Eye of Providence, Rod of Asclepius, Shield of the Phoenix, Draconic Scale,
    Magi''s Cloak, Jade Scepter, Wish-Granting Pearl, Mantle Of Discord, Midgardian
    Mail.'
  slot_scores:
    Book of Thoth:
      total: 0.37
      efficiency: 0.51
      win: 0.36
      pick: 0.13
      fit: 0.13
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.26
      fit: 0.21
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.42
      pick: 0.0
      fit: 0.49
    Transcendence:
      total: 0.4
      efficiency: 0.53
      win: 0.42
      pick: 0.0
      fit: 0.14
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.6
      pick: 0.11
      fit: 0.4
    Amanita Charm:
      total: 0.48
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Rod of Tahuti
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s Revenge, Gluttonous Grimoire,
    Nimble Ring, Amanita Charm, Daybreak Gavel, Soul Gem, Kinetic Cuirass, Freya''s
    Tears, Golden Blade, Riptalon, Spear of the Magus, Spear of Desolation, Silverbranch
    Bow, Helm of Radiance, Runeforged Hammer, Tyrfing, Shield Splitter, Obsidian Shard,
    Lernaean Bow, Pharaoh''s Curse, Toxic Blade, Shogun''s Ofuda, The Reaper, Rod
    of Asclepius, Hydra''s Lament, Stone of Binding, Erosion, Tekko-Kagi, Bragi''s
    Harp, Shield of the Phoenix, Eye of Providence, Eye of the Storm, Bracer of The
    Abyss, Heartseeker, Draconic Scale, Magi''s Cloak, Screeching Gargoyle.'
  slot_scores:
    Golden Blade:
      total: 0.44
      efficiency: 0.52
      win: 0.42
      pick: 0.0
      fit: 0.45
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.5
      pick: 0.26
      fit: 0.17
    Berserker's Shield:
      total: 0.48
      efficiency: 0.68
      win: 0.42
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.72
      win: 0.42
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.47
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.33
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.6
      pick: 0.11
      fit: 0.21
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Gladiator's Shield
  - Freya's Tears
  - Rod of Tahuti
  flex_slots:
  - Breastplate of Valor
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Gladiator''s Shield, Freya''s Tears, Amanita Charm, Daybreak Gavel, Spear of Desolation,
    Kinetic Cuirass, Soul Gem, Shield of the Phoenix, Hydra''s Lament, Screeching
    Gargoyle, Gluttonous Grimoire, Berserker''s Shield, Chronos'' Pendant, Shield
    Splitter, Spear of the Magus, Runeforged Hammer, Helm of Radiance, Prophetic Cloak,
    Erosion, Obsidian Shard, Eye of Providence, Stone of Binding, Draconic Scale,
    Eye of the Storm, Arondight, Gem of Focus, Magi''s Cloak, Rod of Asclepius, Heartseeker,
    Eye of Erebus, Mantle Of Discord, Midgardian Mail, Pendulum Blade, Glorious Pridwen,
    Jade Scepter, Chandra''s Grace, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.26
      fit: 0.43
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.43
      pick: 0.18
      fit: 0.43
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.42
      pick: 0.0
      fit: 0.51
    Gladiator's Shield:
      total: 0.51
      efficiency: 0.39
      win: 0.6
      pick: 0.08
      fit: 0.65
    Freya's Tears:
      total: 0.49
      efficiency: 0.61
      win: 0.42
      pick: 0.0
      fit: 0.58
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.6
      pick: 0.11
      fit: 0.22
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Kinetic
    Cuirass, Freya''s Tears, Gluttonous Grimoire, Shield Splitter, Spear of Desolation,
    Runeforged Hammer, Spear of the Magus, Helm of Radiance, Soul Gem, Berserker''s
    Shield, Obsidian Shard, Eye of the Storm, Erosion, Eye of Providence, Hydra''s
    Lament, Draconic Scale, Heartseeker, Shield of the Phoenix, Stone of Binding,
    Rod of Asclepius, Magi''s Cloak, Avenging Blade, Jade Scepter, Doom Orb, Screeching
    Gargoyle, Wish-Granting Pearl, Mantle Of Discord, Helm of Darkness, Midgardian
    Mail, Titan''s Bane, Death Metal, Chronos'' Pendant, The Crusher, Daybreak Gavel,
    The World Stone, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.26
      fit: 0.24
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.42
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.56
      win: 0.42
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.47
      efficiency: 0.61
      win: 0.42
      pick: 0.0
      fit: 0.4
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.6
      pick: 0.11
      fit: 0.3
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.45
  starter: *id001
---
