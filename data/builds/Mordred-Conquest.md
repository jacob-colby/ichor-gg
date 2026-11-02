---
type: smite-build
god: Mordred
mode: Conquest
builds:
- source: community
  aspect: Aspect of Rage
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.46
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.32
    win_rate: 0.54
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.31
      win_rate: 0.51
    - name: Bracer of The Abyss
      pick_rate: 0.1
      win_rate: 0.6
  - name: Sanguine Lash
    pick_rate: 0.15
    win_rate: 0.58
    alternates:
    - name: Shield of the Phoenix
      pick_rate: 0.1
      win_rate: 0.47
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.51
  - name: Nimble Ring
    pick_rate: 0.12
    win_rate: 0.6
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.48
    - name: Sanguine Lash
      pick_rate: 0.08
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.15
    win_rate: 0.56
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.62
    - name: Kinetic Cuirass
      pick_rate: 0.06
      win_rate: 0.63
  - name: Hide of the Nemean Lion
    pick_rate: 0.07
    win_rate: 0.42
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.63
    - name: Draconic Scale
      pick_rate: 0.05
      win_rate: 0.72
  - name: Medal of Defense
    pick_rate: 0.07
    win_rate: 0.43
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.56
    - name: Killing Stone
      pick_rate: 0.04
      win_rate: 0.71
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.38
    win_rate: 0.62
  - name: Bluestone Pendant
    pick_rate: 0.22
    win_rate: 0.36
  - name: Hunter's Cowl
    pick_rate: 0.16
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/mordred/
  last_verified: '2026-11-02'
  god_win_rate: 0.5480427046263345
  god_matches_won: 308
  god_matches_played: 562
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14484
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Kinetic Cuirass, Jotunn''s Revenge, Amanita Charm, Shield
    Splitter, Berserker''s Shield, Genji''s Guard, Breastplate of Valor, Runeforged
    Hammer, Erosion, Titan''s Bane, Gluttonous Grimoire, Hydra''s Lament, Eye of Providence,
    Spear of Desolation, Obsidian Shard, Stone of Binding, Oni Hunter''s Garb, Helm
    of Darkness, Helm of Radiance, Magi''s Cloak, Soul Gem, Midgardian Mail, Mantle
    Of Discord, Avenging Blade, The Crusher, Screeching Gargoyle, Leviathan''s Hide,
    Heartseeker, Wyrmskin Hide, Arondight, Spear of the Magus, The Reaper, Ancile,
    Stampede, Death Metal, Void Stone, Shield of the Phoenix.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.67
      win: 0.58
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.63
      pick: 0.1
      fit: 0.61
    Shield Splitter:
      total: 0.55
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.56
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.72
      pick: 0.11
      fit: 0.51
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.51
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Draconic Scale
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Draconic Scale, Kinetic Cuirass, Amanita Charm, Genji''s Guard, Shield
    Splitter, Berserker''s Shield, Breastplate of Valor, Spear of Desolation, Gluttonous
    Grimoire, Obsidian Shard, Hydra''s Lament, Soul Gem, Helm of Radiance, Runeforged
    Hammer, Helm of Darkness, Titan''s Bane, Spear of the Magus, Death Metal, Doom
    Orb, Oni Hunter''s Garb, Heartseeker, The World Stone, Chronos'' Pendant, Jade
    Scepter, The Crusher, Erosion, Eye of Providence, Avenging Blade, Stone of Binding,
    Arondight, Wish-Granting Pearl, Screeching Gargoyle, Ancient Signet, Midgardian
    Mail, Polynomicon, Magi''s Cloak, Heartwood Charm, Triton''s Conch, Shield of
    the Phoenix.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.63
      pick: 0.1
      fit: 0.46
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.72
      pick: 0.11
      fit: 0.36
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.87
      win: 0.62
      pick: 0.17
      fit: 0.36
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Spear of Desolation
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, Draconic Scale, Kinetic Cuirass, Amanita Charm, Genji''s
    Guard, Spear of Desolation, Berserker''s Shield, Soul Gem, Gluttonous Grimoire,
    Obsidian Shard, Shield Splitter, Breastplate of Valor, Titan''s Bane, Spear of
    the Magus, Hydra''s Lament, Helm of Radiance, Runeforged Hammer, Helm of Darkness,
    Doom Orb, The Crusher, Screeching Gargoyle, Heartseeker, The World Stone, Erosion,
    Chronos'' Pendant, Eye of Providence, Oni Hunter''s Garb, Stone of Binding, Death
    Metal, Arondight, The Reaper, Midgardian Mail, Magi''s Cloak, Dreamer''s Idol,
    Jade Scepter, Mantle Of Discord, Avenging Blade, Leviathan''s Hide, Shield of
    the Phoenix.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.27
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.63
      pick: 0.1
      fit: 0.48
    Spear of Desolation:
      total: 0.54
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.48
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.72
      pick: 0.11
      fit: 0.38
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Draconic Scale
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Soul Gem
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Draconic Scale, Kinetic Cuirass, Jotunn''s Revenge, Soul
    Gem, Berserker''s Shield, Shield Splitter, Genji''s Guard, The Reaper, Runeforged
    Hammer, Phoenix Feather, Yogi''s Necklace, Gluttonous Grimoire, Breastplate of
    Valor, Ethereal Staff, Titan''s Bane, Hydra''s Lament, Chandra''s Grace, Spear
    of Desolation, Erosion, Shield of the Phoenix, Eye of Providence, Obsidian Shard,
    Oni Hunter''s Garb, Avenging Blade, Midgardian Mail, Blood-Bound Book, The Crusher,
    Helm of Radiance, Glorious Pridwen, Leviathan''s Hide, Regrowth Striders, Heartseeker,
    Rod of Asclepius, Sphere of Negation, Stone of Binding, Wyrmskin Hide, Helm of
    Darkness, Arondight.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.63
      pick: 0.1
      fit: 0.6
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.72
      pick: 0.11
      fit: 0.5
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.87
      win: 0.62
      pick: 0.17
      fit: 0.2
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.55
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Draconic Scale, Kinetic Cuirass, Amanita Charm,
    Stone of Binding, Shield Splitter, Screeching Gargoyle, Avenging Blade, Berserker''s
    Shield, Genji''s Guard, Titan''s Bane, Gluttonous Grimoire, Spear of Desolation,
    Obsidian Shard, Void Stone, Soul Gem, Void Shield, Breastplate of Valor, The Crusher,
    Runeforged Hammer, Heartseeker, Spear of the Magus, The Reaper, Hydra''s Lament,
    Erosion, Eye of Providence, Doom Orb, Helm of Radiance, Oni Hunter''s Garb, The
    World Stone, Tekko-Kagi, Helm of Darkness, Midgardian Mail, Magi''s Cloak, Mantle
    Of Discord, Leviathan''s Hide, Dreamer''s Idol, Avatar''s Parashu, Shield of the
    Phoenix.'
  slot_scores:
    Stone of Binding:
      total: 0.54
      efficiency: 0.5
      win: 0.58
      pick: 0.0
      fit: 0.7
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.63
      pick: 0.1
      fit: 0.52
    Shield Splitter:
      total: 0.54
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.46
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.72
      pick: 0.11
      fit: 0.42
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Nimble Ring
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Draconic Scale, Kinetic Cuirass, Amanita Charm,
    Jotunn''s Revenge, Genji''s Guard, Gluttonous Grimoire, Shield Splitter, Golden
    Blade, Soul Gem, Breastplate of Valor, Tekko-Kagi, Tyrfing, Toxic Blade, Silverbranch
    Bow, Runeforged Hammer, Obsidian Shard, Pharaoh''s Curse, Lernaean Bow, Spear
    of Desolation, The Reaper, Hydra''s Lament, Titan''s Bane, Helm of Radiance, Shogun''s
    Ofuda, Riptalon, Oni Hunter''s Garb, Erosion, Eros'' Bow, Stone of Binding, Eye
    of Providence, Midgardian Mail, Screeching Gargoyle, Magi''s Cloak, Helm of Darkness,
    Mantle Of Discord, Blood-Bound Book, Spear of the Magus, Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.5
    Berserker's Shield:
      total: 0.58
      efficiency: 0.75
      win: 0.58
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.63
      pick: 0.1
      fit: 0.44
    Nimble Ring:
      total: 0.54
      efficiency: 0.64
      win: 0.6
      pick: 0.19
      fit: 0.28
    Draconic Scale:
      total: 0.55
      efficiency: 0.5
      win: 0.72
      pick: 0.11
      fit: 0.34
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.34
  community_ordered:
  - Kinetic Cuirass
  - Nimble Ring
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Amanita Charm
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Draconic Scale, Kinetic Cuirass, Amanita Charm, Breastplate of Valor, Spear of
    Desolation, Soul Gem, Berserker''s Shield, Hydra''s Lament, Shield Splitter, Screeching
    Gargoyle, Gluttonous Grimoire, Chronos'' Pendant, Obsidian Shard, Arondight, Helm
    of Radiance, Runeforged Hammer, Prophetic Cloak, Helm of Darkness, Erosion, Eye
    of Providence, Oni Hunter''s Garb, Stone of Binding, Titan''s Bane, Gem of Focus,
    Gladiator''s Shield, Midgardian Mail, Spear of the Magus, Magi''s Cloak, Heartwood
    Charm, Mantle Of Discord, Leviathan''s Hide, Chandra''s Grace, Eye of Erebus,
    Shield of the Phoenix, Regrowth Striders, Glorious Pridwen, Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.5
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.63
      pick: 0.1
      fit: 0.51
    Freya's Tears:
      total: 0.56
      efficiency: 0.58
      win: 0.56
      pick: 0.25
      fit: 0.59
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.72
      pick: 0.11
      fit: 0.41
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Spear of Desolation
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Jotunn''s Revenge, Draconic Scale, Kinetic
    Cuirass, Amanita Charm, Genji''s Guard, Spear of Desolation, Gluttonous Grimoire,
    Berserker''s Shield, Shield Splitter, Obsidian Shard, Soul Gem, Helm of Radiance,
    Breastplate of Valor, Helm of Darkness, Spear of the Magus, Runeforged Hammer,
    Hydra''s Lament, Titan''s Bane, Death Metal, Chronos'' Pendant, Doom Orb, Jade
    Scepter, The World Stone, Erosion, Eye of Providence, Screeching Gargoyle, Oni
    Hunter''s Garb, Stone of Binding, The Crusher, Midgardian Mail, Magi''s Cloak,
    Dreamer''s Idol, Heartseeker, Arondight, Avenging Blade, Mantle Of Discord, Ethereal
    Staff, Wish-Granting Pearl, Leviathan''s Hide, Shield of the Phoenix.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.63
      pick: 0.1
      fit: 0.49
    Spear of Desolation:
      total: 0.54
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.46
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.72
      pick: 0.11
      fit: 0.39
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Draconic Scale, Jotunn''s Revenge,
    Kinetic Cuirass, Amanita Charm, Shield Splitter, Berserker''s Shield, Genji''s
    Guard, Gluttonous Grimoire, Spear of Desolation, Obsidian Shard, Soul Gem, Helm
    of Radiance, Breastplate of Valor, Runeforged Hammer, Helm of Darkness, Titan''s
    Bane, Spear of the Magus, Hydra''s Lament, Death Metal, Erosion, Eye of Providence,
    Doom Orb, The Crusher, Oni Hunter''s Garb, Stone of Binding, Jade Scepter, Heartseeker,
    The World Stone, Midgardian Mail, Avenging Blade, Magi''s Cloak, Chronos'' Pendant,
    Screeching Gargoyle, Mantle Of Discord, Arondight, The Reaper, Leviathan''s Hide,
    Dreamer''s Idol, Shield of the Phoenix.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.67
      win: 0.58
      pick: 0.0
      fit: 0.27
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.63
      pick: 0.1
      fit: 0.52
    Shield Splitter:
      total: 0.54
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.48
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.72
      pick: 0.11
      fit: 0.42
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, Shield Splitter, Kinetic
    Cuirass, Berserker''s Shield, Genji''s Guard, Breastplate of Valor, Runeforged
    Hammer, Erosion, Titan''s Bane, Gluttonous Grimoire, Hydra''s Lament, Eye of Providence,
    Spear of Desolation, Draconic Scale, Obsidian Shard, Stone of Binding, Shield
    of the Phoenix, Oni Hunter''s Garb, Helm of Darkness, Helm of Radiance, Magi''s
    Cloak, Soul Gem, Midgardian Mail, Mantle Of Discord, Avenging Blade, The Crusher,
    Screeching Gargoyle, Leviathan''s Hide, Heartseeker, Wyrmskin Hide, Arondight,
    Spear of the Magus, The Reaper, Ancile, Stampede, Death Metal, Void Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.28
    Berserker's Shield:
      total: 0.54
      efficiency: 0.67
      win: 0.58
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.63
      pick: 0.1
      fit: 0.61
    Shield Splitter:
      total: 0.55
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.56
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.51
  community_ordered:
  - Kinetic Cuirass
  starter: *id001
---
