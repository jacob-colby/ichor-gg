---
type: smite-build
god: Sun Wukong
mode: Conquest
builds:
- source: community
  aspect: Aspect of Transformation
  aspect_pick_rate: 0.16
  aspect_win_rate: 0.44
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.28
    win_rate: 0.49
    alternates:
    - name: Ancient Signet
      pick_rate: 0.1
      win_rate: 0.6
    - name: Runeforged Hammer
      pick_rate: 0.08
      win_rate: 0.59
  - name: Genji's Guard
    pick_rate: 0.11
    win_rate: 0.43
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.2
      win_rate: 0.53
    - name: Prophetic Cloak
      pick_rate: 0.08
      win_rate: 0.49
  - name: Freya's Tears
    pick_rate: 0.13
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.39
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.56
  - name: Obsidian Shard
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.71
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 0.71
  - name: Dwarven Plate
    pick_rate: 0.06
    win_rate: 0.58
    alternates:
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.4
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.53
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.64
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.57
    - name: Veve Charm
      pick_rate: 0.04
      win_rate: 0.57
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.3
    win_rate: 0.61
  - name: Bluestone Pendant
    pick_rate: 0.3
    win_rate: 0.38
  - name: Sands Of Time
    pick_rate: 0.12
    win_rate: 0.55
  source_url: https://smitebrain.com/gods/sun-wukong/
  last_verified: '2026-08-21'
  god_win_rate: 0.5096618357487923
  god_matches_won: 211
  god_matches_played: 414
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-21'
  god_matches_analyzed: 12786
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield, Amanita Charm,
    Runeforged Hammer, Kinetic Cuirass, Gluttonous Grimoire, Golden Blade, Shield
    Splitter, Eye of the Storm, The Crusher, Death Metal, Pharaoh''s Curse, Avenging
    Blade, Nimble Ring, Shield of the Phoenix, Lernaean Bow, Breastplate of Valor,
    Shogun''s Ofuda, Hydra''s Lament, Spectral Armor, Erosion, Eye of Providence,
    Tyrfing, Mantle Of Discord, Heartseeker, Stone of Binding, Draconic Scale, Leviathan''s
    Hide, The Reaper, Ethereal Staff, Soul Gem, Tekko-Kagi, Bragi''s Harp, Rod of
    Asclepius, Daybreak Gavel, Helm of Radiance, Wyrmskin Hide, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.55
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.57
      win: 0.59
      pick: 0.08
      fit: 0.56
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.6
      pick: 0.2
      fit: 0.29
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.45
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Berserker''s Shield, Kinetic Cuirass,
    Shield of the Phoenix, Jotunn''s Revenge, Runeforged Hammer, Ethereal Staff, Rod
    of Asclepius, Soul Gem, The Reaper, Shield Splitter, Gluttonous Grimoire, Eye
    of the Storm, Phoenix Feather, Pharaoh''s Curse, Golden Blade, Erosion, Breastplate
    of Valor, Eye of Providence, Shogun''s Ofuda, Yogi''s Necklace, Spectral Armor,
    Draconic Scale, The Crusher, Mantle Of Discord, Death Metal, Stone of Binding,
    Chandra''s Grace, Avenging Blade, Nimble Ring, Leviathan''s Hide, Riptalon, Lernaean
    Bow, Hydra''s Lament, Lifebinder, Midgardian Mail, Helm of Radiance, Blood-Bound
    Book.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.64
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.71
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.6
      pick: 0.2
      fit: 0.37
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.84
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Berserker's Shield
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Gluttonous Grimoire, The Crusher,
    Berserker''s Shield, Avenging Blade, Soul Gem, Stone of Binding, Amanita Charm,
    Runeforged Hammer, Heartseeker, Kinetic Cuirass, The Reaper, Spear of the Magus,
    Spear of Desolation, Tekko-Kagi, Titan''s Bane, Void Shield, Screeching Gargoyle,
    Void Stone, Silverbranch Bow, Death Metal, Toxic Blade, Nimble Ring, Breastplate
    of Valor, Shield Splitter, Golden Blade, Riptalon, Doom Orb, The Cosmic Horror,
    Eye of the Storm, Pharaoh''s Curse, The World Stone, Shield of the Phoenix, Avatar''s
    Parashu, Hydra''s Lament, Lernaean Bow, Dreamer''s Idol.'
  slot_scores:
    Avenging Blade:
      total: 0.54
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.72
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.56
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.63
    The Crusher:
      total: 0.55
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.71
      pick: 0.1
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Nimble Ring, Golden Blade, Jotunn''s
    Revenge, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Runeforged Hammer,
    Tyrfing, Pharaoh''s Curse, Riptalon, Shogun''s Ofuda, Lernaean Bow, Silverbranch
    Bow, Toxic Blade, Breastplate of Valor, Soul Gem, The Crusher, Death Metal, Shield
    Splitter, Shield of the Phoenix, Spectral Armor, Tekko-Kagi, Bragi''s Harp, Eye
    of the Storm, Mantle Of Discord, Stone of Binding, Hydra''s Lament, The Reaper,
    Daybreak Gavel, Dominance, Avenging Blade, Helm of Radiance, Ethereal Staff, Leviathan''s
    Hide, Bracer of The Abyss, Rod of Asclepius, Spear of the Magus.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.65
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.19
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.36
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.71
      pick: 0.1
      fit: 0.08
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.29
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Breastplate of Valor, Soul Gem, Shield of the Phoenix, Berserker''s Shield, Amanita
    Charm, Spear of Desolation, Hydra''s Lament, Kinetic Cuirass, Gluttonous Grimoire,
    Runeforged Hammer, Chronos'' Pendant, Screeching Gargoyle, Nimble Ring, Chandra''s
    Grace, Death Metal, Arondight, Gem of Focus, Pharaoh''s Curse, Gladiator''s Shield,
    Eye of Erebus, Helm of Radiance, The Crusher, Ethereal Staff, Totem of Death,
    Rod of Asclepius, Spectral Armor, Shield Splitter, Spear of the Magus, Shogun''s
    Ofuda, Golden Blade, Mantle Of Discord, Stone of Binding, Eye of the Storm, Daybreak
    Gavel, Leviathan''s Hide, Prophetic Cloak.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.31
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.6
      pick: 0.2
      fit: 0.52
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.71
      pick: 0.1
      fit: 0.15
    Soul Gem:
      total: 0.54
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield,
    Amanita Charm, Kinetic Cuirass, Runeforged Hammer, Gluttonous Grimoire, Golden
    Blade, Shield Splitter, Eye of the Storm, The Crusher, Death Metal, Pharaoh''s
    Curse, Avenging Blade, Nimble Ring, Shield of the Phoenix, Lernaean Bow, Breastplate
    of Valor, Shogun''s Ofuda, Hydra''s Lament, Spectral Armor, Erosion, Eye of Providence,
    Tyrfing, Mantle Of Discord, Heartseeker, Stone of Binding, Draconic Scale, Leviathan''s
    Hide, The Reaper, Ethereal Staff, Soul Gem, Tekko-Kagi, Bragi''s Harp, Rod of
    Asclepius, Daybreak Gavel, Helm of Radiance, Wyrmskin Hide, Midgardian Mail.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.55
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.57
      win: 0.59
      pick: 0.08
      fit: 0.56
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.45
  starter: *id001
---
