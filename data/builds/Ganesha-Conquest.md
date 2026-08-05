---
type: smite-build
god: Ganesha
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Triumphant
  aspect_pick_rate: 0.14
  aspect_win_rate: 0.58
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.28
    win_rate: 0.6
    alternates:
    - name: Stampede
      pick_rate: 0.18
      win_rate: 0.44
    - name: Eye of Providence
      pick_rate: 0.08
      win_rate: 0.62
  - name: Stampede
    pick_rate: 0.18
    win_rate: 0.45
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.62
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.47
  - name: Genji's Guard
    pick_rate: 0.18
    win_rate: 0.39
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.56
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.64
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.52
    alternates:
    - name: Spirit Robe
      pick_rate: 0.09
      win_rate: 0.36
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.67
  - name: Freya's Tears
    pick_rate: 0.07
    win_rate: 0.67
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.5
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.43
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.67
    alternates:
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.6
    - name: Olmec Blue
      pick_rate: 0.05
      win_rate: 0.75
  source_url: https://smitebrain.com/gods/ganesha/
  last_verified: '2026-08-01'
  god_win_rate: 0.5375722543352601
  god_matches_won: 93
  god_matches_played: 173
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Oni Hunter's Garb
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Kinetic Cuirass, Amanita Charm, Eye of Providence, Gluttonous
    Grimoire, Oni Hunter''s Garb, Shifter''s Shield, Shield of the Phoenix, Erosion,
    Spectral Armor, Draconic Scale, Mantle Of Discord, Breastplate of Valor, Ethereal
    Staff, Leviathan''s Hide, Soul Gem, Hussar''s Wings, Yogi''s Necklace, Midgardian
    Mail, Hide of the Nemean Lion, Wish-Granting Pearl, Gladiator''s Shield, Doublet
    of Binding, Jade Scepter, Chandra''s Grace, Rod of Asclepius.'
  slot_scores:
    Eye of Providence:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.7
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.8
    Oni Hunter's Garb:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.67
      pick: 0.07
      fit: 0.65
    Shifter's Shield:
      total: 0.53
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.7
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Oni Hunter's Garb
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Shield of the Phoenix, Kinetic Cuirass,
    Eye of Providence, Gluttonous Grimoire, Soul Gem, Chandra''s Grace, Rod of Asclepius,
    Oni Hunter''s Garb, Shifter''s Shield, Spectral Armor, Ethereal Staff, Erosion,
    Draconic Scale, Phoenix Feather, Breastplate of Valor, Lifebinder, Mantle Of Discord,
    Yogi''s Necklace, Leviathan''s Hide, Bancroft''s Talon, Blood-Bound Book, Wish-Granting
    Pearl, Spirit Robe, Jade Scepter.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.68
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.78
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.93
    Oni Hunter's Garb:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.67
      pick: 0.07
      fit: 0.58
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.98
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Eye of Providence
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Oni Hunter's Garb
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Freya''s Tears, Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Soul Gem, Eye of Providence, Oni Hunter''s Garb, Stone of Binding, Spectral Armor,
    Void Shield, Shield of the Phoenix, Spear of the Magus, Breastplate of Valor,
    Ethereal Staff, Shifter''s Shield, Screeching Gargoyle, Mantle Of Discord, Erosion,
    Void Stone, The Cosmic Horror, Draconic Scale, Yogi''s Necklace, Spear of Desolation,
    Leviathan''s Hide, Wish-Granting Pearl, Obsidian Shard.'
  slot_scores:
    Stone of Binding:
      total: 0.5
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.75
    Eye of Providence:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.49
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.59
    Oni Hunter's Garb:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.31
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.67
      pick: 0.07
      fit: 0.45
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Oni Hunter''s Garb, Eye of Providence, Ethereal Staff, Spectral Armor, Breastplate
    of Valor, Soul Gem, Shield of the Phoenix, Mantle Of Discord, Yogi''s Necklace,
    Shifter''s Shield, Bracer of The Abyss, Bragi''s Harp, Erosion, Death Metal, Draconic
    Scale, Wish-Granting Pearl, Leviathan''s Hide, Jade Scepter, Rod of Asclepius,
    Nimble Ring, Chandra''s Grace, Midgardian Mail.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.46
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.3
    Bragi's Harp:
      total: 0.48
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.67
      pick: 0.07
      fit: 0.33
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Eye of Providence
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Oni Hunter's Garb
  - Freya's Tears
  flex_slots:
  - Eye of Providence
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Kinetic Cuirass, Breastplate
    of Valor, Shield of the Phoenix, Amanita Charm, Gluttonous Grimoire, Soul Gem,
    Eye of Providence, Oni Hunter''s Garb, Ethereal Staff, Chandra''s Grace, Spectral
    Armor, Shifter''s Shield, Chronos'' Pendant, Mantle Of Discord, Gladiator''s Shield,
    Erosion, Yogi''s Necklace, Screeching Gargoyle, Draconic Scale, Wish-Granting
    Pearl, Jade Scepter, Death Metal, Leviathan''s Hide, Rod of Asclepius, Gem of
    Focus.'
  slot_scores:
    Eye of Providence:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.61
    Oni Hunter's Garb:
      total: 0.51
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.29
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.67
      pick: 0.07
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Runeforged Hammer
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Freya''s Tears, The Crusher, Gluttonous Grimoire,
    Jotunn''s Revenge, Berserker''s Shield, Runeforged Hammer, Hydra''s Lament, Kinetic
    Cuirass, Amanita Charm, Eye of Providence, Lernaean Bow, Oni Hunter''s Garb, Avenging
    Blade, Golden Blade, Shield Splitter, Soul Gem, Pharaoh''s Curse, Eye of the Storm,
    Spectral Armor, Ethereal Staff, Breastplate of Valor, Shield of the Phoenix, Death
    Metal, Mantle Of Discord, Shifter''s Shield, Damaru, The Reaper, Yogi''s Necklace,
    Erosion, Heartseeker, Draconic Scale, Bragi''s Harp, Shogun''s Ofuda, Triton''s
    Conch, Arondight, Leviathan''s Hide, Wish-Granting Pearl, Avatar''s Parashu.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.45
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.67
      pick: 0.07
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.41
    The Crusher:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.46
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Runeforged Hammer
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Gluttonous Grimoire,
    The Crusher, Jotunn''s Revenge, Runeforged Hammer, Kinetic Cuirass, Amanita Charm,
    Berserker''s Shield, Hydra''s Lament, Soul Gem, Ethereal Staff, Eye of Providence,
    Oni Hunter''s Garb, Death Metal, Avenging Blade, Shield Splitter, Spectral Armor,
    Breastplate of Valor, Eye of the Storm, Wish-Granting Pearl, Shield of the Phoenix,
    Lernaean Bow, Jade Scepter, Mantle Of Discord, Triton''s Conch, Spear of the Magus,
    Shifter''s Shield, Rod of Asclepius, Pharaoh''s Curse, Golden Blade, Yogi''s Necklace,
    Erosion, Helm of Radiance, Damaru, The Reaper, Draconic Scale, The Cosmic Horror,
    Bragi''s Harp.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.51
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.39
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.67
      pick: 0.07
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.54
    The Crusher:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Oni Hunter's Garb
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Eye of Providence, Gluttonous
    Grimoire, Oni Hunter''s Garb, Shifter''s Shield, Freya''s Tears, Shield of the
    Phoenix, Erosion, Spectral Armor, Draconic Scale, Mantle Of Discord, Breastplate
    of Valor, Ethereal Staff, Leviathan''s Hide, Soul Gem, Hussar''s Wings, Yogi''s
    Necklace, Midgardian Mail, Hide of the Nemean Lion, Wish-Granting Pearl, Gladiator''s
    Shield, Doublet of Binding, Jade Scepter, Chandra''s Grace, Rod of Asclepius.'
  slot_scores:
    Eye of Providence:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.7
    Genji's Guard:
      total: 0.5
      efficiency: 0.74
      win: 0.39
      pick: 0.18
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.8
    Oni Hunter's Garb:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.45
    Shifter's Shield:
      total: 0.53
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.7
  starter: *id001
---
